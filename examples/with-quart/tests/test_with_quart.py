# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Smoke tests for the Quart FastUI example."""

# ruff: file-ignore[assert]

import asyncio
import json
from http import HTTPStatus

from with_quart import app


async def _get(path: str) -> tuple[int, str]:
    response = await app.test_client().get(path)
    return response.status_code, (await response.get_data(as_text=True))


def test_api_returns_fastui_json() -> None:
    """Serve the component tree as JSON."""
    status, body = asyncio.run(_get("/api/"))

    assert status == HTTPStatus.OK
    assert json.loads(body) == [{"type": "Heading", "text": "Hello World", "level": 1}]


def test_other_paths_serve_the_react_shell() -> None:
    """Serve the prebuilt HTML for any non-API path."""
    for path in ("/", "/some/deep/path"):
        status, body = asyncio.run(_get(path))

        assert status == HTTPStatus.OK
        assert "<html" in body
