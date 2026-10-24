# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Smoke tests for the Emmett FastUI example."""

# ruff: file-ignore[assert]

import json
from http import HTTPStatus

from emmett.testing import EmmettTestClient
from with_emmett import app


def test_api_returns_fastui_json() -> None:
    """Serve the component tree as JSON."""
    response = EmmettTestClient(app).get("/api/")

    assert response.status == HTTPStatus.OK
    assert response.headers["content-type"].startswith("application/json")
    assert json.loads(response.data) == [
        {"type": "Heading", "text": "Hello World", "level": 1},
    ]


def test_other_paths_serve_the_react_shell() -> None:
    """Serve the prebuilt HTML for any non-API path."""
    client = EmmettTestClient(app)
    for path in ("/", "/some/deep/path"):
        response = client.get(path)

        assert response.status == HTTPStatus.OK
        assert response.headers["content-type"].startswith("text/html")
        assert "<html" in response.data
