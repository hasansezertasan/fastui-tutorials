# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Smoke tests for the Bottle FastUI example."""

# ruff: file-ignore[assert]

import json
from io import BytesIO
from wsgiref.util import setup_testing_defaults

from with_bottle import app

OK = "200"


def get(path: str) -> tuple[str, dict[str, str], str]:
    """Call the WSGI app with a GET request.

    Returns:
        The status line, response headers and decoded body.
    """
    environ = {"REQUEST_METHOD": "GET", "PATH_INFO": path, "wsgi.input": BytesIO()}
    setup_testing_defaults(environ)
    captured: dict = {}

    def start_response(
        status: str,
        headers: list[tuple[str, str]],
        exc_info: object = None,
    ) -> None:
        captured["status"] = status
        captured["headers"] = {k.lower(): v for k, v in headers}

    body = b"".join(app(environ, start_response)).decode()
    return captured["status"], captured["headers"], body


def test_api_returns_fastui_json() -> None:
    """Serve the component tree as JSON."""
    status, headers, body = get("/api/")

    assert status.startswith(OK)
    assert headers["content-type"].startswith("application/json")
    assert json.loads(body) == [{"type": "Heading", "text": "Hello World", "level": 1}]


def test_other_paths_serve_the_react_shell() -> None:
    """Serve the prebuilt HTML for any non-API path."""
    for path in ("/", "/some/deep/path"):
        status, _, body = get(path)

        assert status.startswith(OK)
        assert "<html" in body
