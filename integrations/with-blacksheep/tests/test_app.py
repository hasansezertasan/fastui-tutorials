# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Tests for the BlackSheep FastUI integration."""

# ruff: noqa: S101

import asyncio
import json
from typing import TYPE_CHECKING, cast

from blacksheep.testing import TestClient
from with_blacksheep import app

if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable

HTTP_OK = 200


def test_blacksheep_app_serves_fastui_api_and_shell() -> None:
    """Serve FastUI JSON at `/api/` and the HTML shell for app paths."""

    async def run() -> None:
        start = cast("Callable[[], Awaitable[None]]", app.start)
        await start()
        client = TestClient(app)

        api_response = await client.get("/api/")
        assert api_response.status == HTTP_OK
        api_content = api_response.content
        assert api_content is not None
        assert api_content.type == b"application/json"
        assert json.loads(api_content.body) == [
            {
                "class_name": None,
                "html_id": None,
                "level": 1,
                "text": "Hello World",
                "type": "Heading",
            },
        ]

        shell_response = await client.get("/docs/anything")
        assert shell_response.status == HTTP_OK
        shell_content = shell_response.content
        assert shell_content is not None
        assert shell_content.type == b"text/html; charset=utf-8"
        assert b"FastUI and BlackSheep Example" in shell_content.body

    asyncio.run(run())
