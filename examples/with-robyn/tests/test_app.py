# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Tests for the Robyn FastUI example."""

# ruff: file-ignore[assert]

from typing import TYPE_CHECKING, Any, cast

import pytest

pytest.importorskip("robyn", reason="robyn is not installed")

from robyn.robyn import HttpMethod
from with_robyn import app, page

if TYPE_CHECKING:
    from collections.abc import Callable

    from robyn import Request


def test_robyn_app_registers_api_root_and_shell_routes() -> None:
    """Register API, root, and wildcard shell routes in matching order."""
    routes = [
        route.route
        for route in app.router.get_routes()
        if route.route_type == HttpMethod.GET
    ]

    # Check for presence and relative ordering of critical routes
    # API should come before root/wildcard to avoid being shadowed.
    # Robyn normalizes the registered path, so "/api/" is stored as "/api".
    expected_order = ["/api", "/", "/*path"]
    actual_order = [r for r in routes if r in expected_order]

    assert actual_order == expected_order


def test_robyn_api_route_returns_fastui_json() -> None:
    """Serialize the FastUI component tree for the API route."""
    handler = cast("Callable[[Request], list[Any]]", page)

    # Robyn serializes the returned list to JSON itself, so the handler
    # returns the component tree as plain Python objects.
    assert handler(cast("Request", object())) == [
        {"level": 1, "text": "Hello World", "type": "Heading"},
    ]
