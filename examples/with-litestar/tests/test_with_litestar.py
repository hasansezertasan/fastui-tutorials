# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Smoke tests for the Litestar FastUI example."""

# ruff: file-ignore[assert]

from http import HTTPStatus

from litestar.testing import TestClient
from with_litestar import app


def test_api_returns_fastui_json_without_nulls() -> None:
    """Serialize the component tree without unset fields."""
    with TestClient(app) as client:
        response = client.get("/api/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == [{"type": "Heading", "text": "Hello World", "level": 1}]


def test_other_paths_serve_the_react_shell() -> None:
    """Serve the prebuilt HTML for any non-API path."""
    with TestClient(app) as client:
        for path in ("/", "/some/deep/path"):
            response = client.get(path)

            assert response.status_code == HTTPStatus.OK
            assert "<html" in response.text
