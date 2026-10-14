# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
from __future__ import annotations

import asyncio
import logging
import os
import re
from typing import TYPE_CHECKING
from urllib.parse import quote_plus

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.components.display import DisplayLookup, DisplayMode
from fastui.events import GoToEvent, PageEvent
from pydantic import BaseModel, Field
from pydantic_ai import Agent, ModelMessage, ModelResponse, TextPart
from pydantic_ai.exceptions import ModelAPIError, UserError
from pydantic_ai.models.fallback import FallbackModel
from pydantic_ai.models.function import AgentInfo, FunctionModel
from starlette.responses import StreamingResponse

if TYPE_CHECKING:
    from collections.abc import AsyncIterable

FastUI.model_rebuild()

logger = logging.getLogger(__name__)

app = FastAPI()


def _echo_model(messages: list[ModelMessage], _info: AgentInfo) -> ModelResponse:
    """Offline fallback: echo the last user prompt without any API key."""
    user_text = ""
    for message in reversed(messages):
        for part in message.parts:
            if part.part_kind == "user-prompt" and isinstance(part.content, str):
                user_text = part.content
                break
        if user_text:
            break
    text = (
        f"Echo: {_escape_markdown(user_text)}\n\n"
        "Set `OPENAI_API_KEY` (and optionally `PYDANTIC_AI_MODEL`) "
        "to get real ChatGPT-style replies via pydantic-ai."
    )
    return ModelResponse(parts=[TextPart(text)])


async def _echo_stream(
    messages: list[ModelMessage],
    _info: AgentInfo,
) -> AsyncIterable[str]:
    """Stream the echo fallback word-by-word so SSE still demos streaming.

    Yields:
        One word (with trailing space) per iteration.
    """
    response = _echo_model(messages, _info)
    first_part = response.parts[0]
    text = first_part.content if isinstance(first_part, TextPart) else ""
    for word in text.split(" "):
        yield word + " "
        await asyncio.sleep(0.02)


def _build_agent() -> Agent[None, str]:
    primary = os.getenv("PYDANTIC_AI_MODEL", "openai:gpt-4o-mini")
    echo = FunctionModel(_echo_model, stream_function=_echo_stream)
    try:
        model = FallbackModel(primary, echo, fallback_on=(ModelAPIError, UserError))
    except UserError:
        # E.g. no API key for the configured provider: offline echo mode.
        model = echo
    return Agent(
        model,
        instructions="You are a helpful chatbot.",
    )


agent: Agent[None, str] = _build_agent()


class MessageHistoryModel(BaseModel):
    message: str = Field(title="Message")


class ChatForm(BaseModel):
    chat: str = Field(title=" ", max_length=1000)


# In-memory demo state (resets on restart, like the koyeb example).
# Single-user demo: every visitor shares these lists, so do not expose
# this beyond localhost without per-session state.
message_history: list[ModelMessage] = []
display_history: list[MessageHistoryModel] = []


# Epoch counter: bumped on reset so an in-flight stream that finishes
# after a reset does not restore cleared history.
class _HistoryEpoch:
    value = 0


# Bounds for the in-memory demo history (messages alternate user/assistant).
MAX_HISTORY_MESSAGES = 100
MAX_HISTORY_EXCHANGES = 50

_MARKDOWN_SPECIALS = re.compile(r"([\\`*_{}\[\]()#+\-.!|<>~=])")


def _escape_markdown(text: str) -> str:
    """Escape Markdown metacharacters so user input renders literally."""
    return _MARKDOWN_SPECIALS.sub(r"\\\1", text)


def _trim_histories() -> None:
    """Bound in-memory demo history (and the LLM context derived from it)."""
    del message_history[:-MAX_HISTORY_MESSAGES]
    del display_history[:-MAX_HISTORY_EXCHANGES]


def _sse_message(text: str) -> str:
    """Wrap rendered Markdown in a server-sent event."""
    m = FastUI(root=[c.Markdown(text=text)])
    return f"data: {m.model_dump_json(by_alias=True, exclude_none=True)}\n\n"


async def _stream_agent_text(prompt: str) -> AsyncIterable[str]:
    """Stream reply deltas from the agent.

    Yields:
        One delta chunk of the reply per iteration; the caller accumulates.
    """
    # Same pattern as the official pydantic-ai chat-app docs: yielding inside
    # `run_stream` is how token streaming works; the context manager ends
    # normally once the stream is exhausted.
    generation = _HistoryEpoch.value
    async with agent.run_stream(prompt, message_history=message_history) as result:
        async for chunk in result.stream_text(delta=True):
            yield chunk  # ruff: ignore[yield-in-context-manager-in-async-generator] - token streaming per pydantic-ai docs
        # Persist pydantic-ai history for multi-turn context. `stream_text`
        # records the final response on completion, so `new_messages()` holds
        # the user request plus the assistant reply (covered by
        # `test_ai_response_generator_streams_reply`).
        if generation != _HistoryEpoch.value:
            # A reset cleared history mid-stream: do not restore it.
            return
        message_history.extend(result.new_messages())
        _trim_histories()


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
async def api_index(
    chat: str | None = None,
    *,
    reset: bool = False,
) -> list[AnyComponent]:
    # Async so reset runs on the event loop: the epoch check and the history
    # mutation in the streaming generator have no `await` between them, so a
    # reset cannot interleave and be silently undone.
    if reset:
        message_history.clear()
        display_history.clear()
        _HistoryEpoch.value += 1

    sse_path = "/api/sse"
    if chat:
        sse_path += f"?prompt={quote_plus(chat)}"

    return [
        c.PageTitle(text="FastUI Chatbot (pydantic-ai)"),
        c.Page(
            components=[
                c.Heading(text="FastUI Chatbot"),
                c.Paragraph(
                    text="ChatGPT-style chatbot built with FastUI and pydantic-ai. "
                    "Without an API key it echoes; set OPENAI_API_KEY for real replies.",
                ),
                c.Table(
                    data=display_history,
                    data_model=MessageHistoryModel,
                    columns=[
                        DisplayLookup(
                            field="message",
                            mode=DisplayMode.markdown,
                            table_width_percent=100,
                        ),
                    ],
                    no_data_message="No messages yet.",
                ),
                c.ModelForm(model=ChatForm, submit_url=".", method="GOTO"),
                c.Link(
                    components=[c.Text(text="Reset Chat")],
                    on_click=GoToEvent(url="/?reset=true"),
                ),
                c.Div(
                    components=[
                        c.ServerLoad(
                            path=sse_path,
                            sse=True,
                            load_trigger=PageEvent(name="load"),
                            components=[],
                        ),
                    ],
                    class_name="my-2 p-2 border rounded",
                ),
            ],
        ),
        c.Footer(extra_text="Made with FastUI + pydantic-ai", links=[]),
    ]


@app.get("/api/sse")
async def sse_ai_response(prompt: str | None = None) -> StreamingResponse:
    if not prompt:
        return StreamingResponse(empty_response(), media_type="text/event-stream")
    return StreamingResponse(
        ai_response_generator(prompt),
        media_type="text/event-stream",
    )


async def empty_response() -> AsyncIterable[str]:
    """Yield an empty Markdown event forever to keep the SSE connection open.

    Yields:
        The same empty event on each iteration.
    """
    msg = _sse_message("")
    yield msg
    # Avoid the browser reconnecting.
    while True:
        yield msg
        await asyncio.sleep(10)


async def ai_response_generator(prompt: str) -> AsyncIterable[str]:
    """Stream the agent reply as Markdown server-sent events.

    `FallbackModel` converts failures while opening the provider stream into
    echo replies, but mid-stream failures propagate, so they are caught here
    and surfaced as a terminal error event. A failed exchange is shown in the
    display history but intentionally left out of `message_history` to keep
    the LLM context clean.

    Yields:
        One server-sent event per streamed chunk, then the last event forever.
    """
    generation = _HistoryEpoch.value
    output = f"**User:** {_escape_markdown(prompt)}\n\n**Chatbot:** "
    msg = _sse_message(output)
    try:
        async for chunk in _stream_agent_text(prompt):
            output += chunk
            msg = _sse_message(output)
            yield msg
    except Exception:
        logger.exception("Chatbot stream failed mid-response")
        output += "\n\n⚠️ Reply interrupted by a provider error; please retry."
        msg = _sse_message(output)
        yield msg

    if generation == _HistoryEpoch.value:
        display_history.append(MessageHistoryModel(message=output))
        _trim_histories()
    # Avoid the browser reconnecting.
    while True:
        yield msg
        await asyncio.sleep(10)


@app.get("/{path:path}")
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="FastUI Chatbot (pydantic-ai)"))


def main() -> None:
    """Run the example with Uvicorn."""
    uvicorn.run("chatgpt:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
