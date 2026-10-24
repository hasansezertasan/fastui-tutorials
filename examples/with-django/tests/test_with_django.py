# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Smoke tests for the Django FastUI example."""

# ruff: file-ignore[assert]

from http import HTTPStatus

import with_django  # ruff: ignore[unused-import]  # configures settings before django.test is imported
from django.test import Client


def test_api_returns_fastui_json() -> None:
    """Serve the component tree as JSON."""
    response = Client().get("/api/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == [{"type": "Heading", "text": "Hello World", "level": 1}]


def test_other_paths_serve_the_react_shell() -> None:
    """Serve the prebuilt HTML for any non-API path."""
    client = Client()
    for path in ("/", "/some/deep/path"):
        response = client.get(path)

        assert response.status_code == HTTPStatus.OK
        assert "<html" in response.content.decode()
