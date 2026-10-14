# ChatGPT-style Chatbot (FastUI + pydantic-ai)

ChatGPT-like chatbot built with [FastUI][fastui] and [pydantic-ai][pydantic-ai].

Inspired by:

- [shroominic/fastui-chat](https://github.com/shroominic/fastui-chat)
- [mem15381/Fastui-chat `chat.py`](https://github.com/mem15381/Fastui-chat/blob/main/src/fastui_chat/chat.py)
- [koyeb/example-fastui-chatbot](https://github.com/koyeb/example-fastui-chatbot)
  (SSE + `ModelForm` + `Table` pattern reused here)
- [pydantic-ai chat app](https://pydantic.dev/docs/ai/examples/chat-app)
  (`run_stream` + `message_history` pattern reused here)

Used Components:

- `PageTitle`
- `Page`
- `Heading`
- `Paragraph`
- `Table` (chat history, markdown mode)
- `ModelForm` (chat input, `GOTO` submit)
- `Link` (reset chat)
- `ServerLoad` (SSE streaming response)
- `Markdown` (streamed reply)
- `Footer`

## How it works

1. `GET /api/` renders history `Table` + input `ModelForm` + empty `ServerLoad` (SSE).
2. Submitting the form `GOTO`s `/?chat=...`, which points `ServerLoad` at `/api/sse?prompt=...`.
3. `GET /api/sse` runs `agent.run_stream(prompt, message_history=...)` and streams
   `Markdown` chunks as server-sent events.
4. After the stream finishes, the exchange is appended to the history `Table`
   and `message_history` keeps multi-turn context.

No API key needed for the demo: without one the agent runs an offline echo
model, and with one a pydantic-ai `FallbackModel` still degrades to echo on
API failures (bad key, no network, rate limit). Either way the reply streams.
Set the key for real replies.

Single-user demo: history is kept in process memory (capped at the last 50
exchanges) and shared by all visitors — do not expose this beyond localhost
without per-session state.

## How to run

### Change directory to the example

```shell
cd examples/chatgpt
```

### Run the application (offline echo mode)

```shell
uv run chatgpt
```

Then open `http://127.0.0.1:8000`.

### Run with a real model

```shell
export OPENAI_API_KEY="..."
export PYDANTIC_AI_MODEL="openai:gpt-4o-mini"  # optional, this is the default
uv run chatgpt
```

Any pydantic-ai model string works, e.g. `anthropic:claude-sonnet-4-6`
(with the matching API key set).

<!-- Links -->
[fastui]: https://github.com/pydantic/FastUI
[pydantic-ai]: https://github.com/pydantic/pydantic-ai
