# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Smoke tests for the Sanic FastUI example."""

# ruff: file-ignore[assert]

import json
from http import HTTPStatus

from with_sanic import app


def test_api_returns_fastui_json() -> None:
    """Serve the component tree as JSON."""
    _, response = app.test_client.get("/api/")

    assert response.status == HTTPStatus.OK
    assert json.loads(response.text) == [
        {"type": "Heading", "text": "Hello World", "level": 1},
    ]


def test_other_paths_serve_the_react_shell() -> None:
    """Serve the prebuilt HTML for any non-API path."""
    for path in ("/", "/some/deep/path"):
        _, response = app.test_client.get(path)

        assert response.status == HTTPStatus.OK
        assert "<html" in response.text
