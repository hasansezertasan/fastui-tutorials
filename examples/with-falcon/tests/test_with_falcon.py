# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Smoke tests for the Falcon FastUI example."""

# ruff: file-ignore[assert]

from http import HTTPStatus

from falcon import testing
from with_falcon import app


def test_api_returns_fastui_json() -> None:
    """Serve the component tree as JSON."""
    result = testing.TestClient(app).simulate_get("/api/")

    assert result.status_code == HTTPStatus.OK
    assert result.json == [{"type": "Heading", "text": "Hello World", "level": 1}]


def test_other_paths_serve_the_react_shell() -> None:
    """Serve the prebuilt HTML for any non-API path."""
    client = testing.TestClient(app)
    for path in ("/", "/some/deep/path"):
        result = client.simulate_get(path)

        assert result.status_code == HTTPStatus.OK
        assert "<html" in result.text
