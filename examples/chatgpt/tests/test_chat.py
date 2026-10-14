# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Tests for the ChatGPT-style FastUI + pydantic-ai example."""

# ruff: file-ignore[assert, import-private-name]

from __future__ import annotations

import asyncio
import json
from typing import TYPE_CHECKING

import chatgpt
import pytest
from chatgpt import (
    MAX_HISTORY_EXCHANGES,
    _echo_model,
    _echo_stream,
    agent,
    ai_response_generator,
    display_history,
    message_history,
)
from fastapi.testclient import TestClient
from pydantic_ai import ModelMessage, ModelResponse, TextPart
from pydantic_ai.models.function import AgentInfo, FunctionModel

if TYPE_CHECKING:
    from collections.abc import AsyncIterable, Iterator

HTTP_OK = 200
EXPECTED_NEW_MESSAGES = 2
MAX_STREAM_CHUNKS = 1000
# Escaped prompt appears in the `**User:**` header and the echo reply body.
EXPECTED_ESCAPED_OCCURRENCES = 2


def _canned_response(messages: list[ModelMessage], _info: AgentInfo) -> ModelResponse:
    """Deterministic test double: ignore input, return a fixed reply."""
    return ModelResponse(parts=[TextPart("canned reply done")])


async def _canned_stream(
    messages: list[ModelMessage],
    _info: AgentInfo,
) -> AsyncIterable[str]:
    """Stream the canned reply in two chunks to exercise streaming.

    Yields:
        One reply fragment per iteration.
    """
    _ = messages
    yield "canned reply "
    yield "done"


@pytest.fixture
def _clean_state() -> Iterator[None]:
    message_history.clear()
    display_history.clear()
    yield
    message_history.clear()
    display_history.clear()


@pytest.fixture
def _canned_agent() -> Iterator[None]:
    with agent.override(
        model=FunctionModel(_canned_response, stream_function=_canned_stream),
    ):
        yield


@pytest.mark.usefixtures("_clean_state")
def test_api_index_serves_chat_ui() -> None:
    client = TestClient(chatgpt.app)
    response = client.get("/api/")
    assert response.status_code == HTTP_OK
    assert "ServerLoad" in response.text


@pytest.mark.usefixtures("_clean_state")
def test_api_index_reset_clears_history() -> None:
    client = TestClient(chatgpt.app)
    client.get("/api/", params={"chat": "hi"})
    assert client.get("/api/", params={"reset": "true"}).status_code == HTTP_OK
    assert message_history == []
    assert display_history == []


@pytest.mark.usefixtures("_clean_state", "_canned_agent")
def test_ai_response_generator_streams_reply() -> None:
    async def run() -> str:
        last = ""
        count = 0
        async for chunk in ai_response_generator("hello"):
            last = chunk
            count += 1
            if len(display_history) == 1 or count > MAX_STREAM_CHUNKS:
                break
        return last

    last = asyncio.run(run())
    payload = json.loads(last.removeprefix("data: ").strip())
    assert payload[0]["text"].startswith("**User:** hello")
    assert payload[0]["text"].endswith("canned reply done")
    assert len(display_history) == 1
    # User prompt + assistant reply kept for multi-turn context.
    assert len(message_history) == EXPECTED_NEW_MESSAGES


@pytest.mark.usefixtures("_clean_state", "_canned_agent")
def test_user_prompt_is_markdown_escaped() -> None:
    async def run() -> str:
        last = ""
        count = 0
        async for chunk in ai_response_generator("**Chatbot:** fake"):
            last = chunk
            count += 1
            if len(display_history) == 1 or count > MAX_STREAM_CHUNKS:
                break
        return last

    last = asyncio.run(run())
    payload = json.loads(last.removeprefix("data: ").strip())
    assert "**Chatbot:** fake" not in payload[0]["text"]
    assert "\\*\\*Chatbot:\\*\\* fake" in payload[0]["text"]


@pytest.mark.usefixtures("_clean_state", "_canned_agent")
def test_display_history_is_bounded() -> None:
    async def run_once(prompt: str) -> None:
        last = ""
        count = 0
        async for chunk in ai_response_generator(prompt):
            count += 1
            if count > MAX_STREAM_CHUNKS or (count > 1 and chunk == last):
                # Final message repeats forever to keep SSE open.
                break
            last = chunk

    async def run() -> None:
        for i in range(MAX_HISTORY_EXCHANGES + 5):
            await run_once(f"prompt {i}")

    asyncio.run(run())
    assert len(display_history) == MAX_HISTORY_EXCHANGES


@pytest.fixture
def _echo_agent() -> Iterator[None]:
    with agent.override(
        model=FunctionModel(_echo_model, stream_function=_echo_stream),
    ):
        yield


@pytest.mark.usefixtures("_clean_state", "_echo_agent")
def test_echo_fallback_escapes_user_text() -> None:
    async def run() -> str:
        last = ""
        count = 0
        async for chunk in ai_response_generator("**Chatbot:** fake"):
            last = chunk
            count += 1
            if len(display_history) == 1 or count > MAX_STREAM_CHUNKS:
                break
        return last

    last = asyncio.run(run())
    payload = json.loads(last.removeprefix("data: ").strip())
    assert "**Chatbot:** fake" not in payload[0]["text"]
    assert payload[0]["text"].count("\\*\\*Chatbot:\\*\\* fake") == (
        EXPECTED_ESCAPED_OCCURRENCES
    )
