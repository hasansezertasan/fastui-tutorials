# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Smoke tests for the Tornado FastUI example."""

# ruff: file-ignore[assert]

import json
from http import HTTPStatus

from tornado.testing import AsyncHTTPTestCase
from with_tornado import make_app


class TestWithTornado(AsyncHTTPTestCase):
    """Exercise the application through a real local HTTP server."""

    def get_app(self):  # ruff: ignore[missing-return-type-undocumented-public-function]
        """Build the application under test."""
        return make_app()

    def test_api_returns_fastui_json(self) -> None:
        """Serve the component tree as JSON."""
        response = self.fetch("/api/")

        assert response.code == HTTPStatus.OK
        assert json.loads(response.body) == [
            {"type": "Heading", "text": "Hello World", "level": 1},
        ]

    def test_other_paths_serve_the_react_shell(self) -> None:
        """Serve the prebuilt HTML for any non-API path."""
        for path in ("/", "/some/deep/path"):
            response = self.fetch(path)

            assert response.code == HTTPStatus.OK
            assert b"<html" in response.body
