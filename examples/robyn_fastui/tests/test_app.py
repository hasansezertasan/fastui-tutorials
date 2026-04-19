# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""Tests for the Robyn FastUI example."""

# ruff: noqa: S101

import json
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from types import ModuleType
from typing import TYPE_CHECKING, cast

from robyn.robyn import HttpMethod

if TYPE_CHECKING:
    from collections.abc import Callable

    from robyn import Request, Robyn


def load_example_module() -> ModuleType:
    """Load the example module from its file path.

    Raises:
        ImportError: If the example module spec cannot be loaded.
    """
    module_path = Path(__file__).parents[1] / "app.py"
    spec = spec_from_file_location("robyn_fastui_app", module_path)
    if spec is None or spec.loader is None:
        msg = f"Unable to load module from {module_path}"
        raise ImportError(msg)

    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_robyn_app_registers_api_root_and_shell_routes() -> None:
    """Register API, root, and wildcard shell routes in matching order."""
    module = load_example_module()
    app = cast("Robyn", module.app)
    routes = [(route.route_type, route.route) for route in app.router.get_routes()]

    assert routes == [
        (HttpMethod.GET, "/api/"),
        (HttpMethod.GET, "/"),
        (HttpMethod.GET, "/*path"),
    ]


def test_robyn_api_route_returns_fastui_json() -> None:
    """Serialize the FastUI component tree for the API route."""
    module = load_example_module()
    page = cast("Callable[[Request], object]", module.page)

    response = page(cast("Request", object()))
    description = cast("bytes", response.description)

    assert json.loads(description) == [
        {
            "class_name": None,
            "html_id": None,
            "level": 1,
            "text": "Hello World",
            "type": "Heading",
        },
    ]
