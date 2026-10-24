# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""FastUI integration example for Pyramid."""

from __future__ import annotations

from typing import TYPE_CHECKING
from wsgiref.simple_server import make_server

from fastui import FastUI, prebuilt_html
from fastui import components as c
from pyramid.config import Configurator
from pyramid.response import Response

if TYPE_CHECKING:
    from pyramid.request import Request

FastUI.model_rebuild()


def page(request: Request) -> Response:
    """Return the FastUI component tree.

    Returns:
        A JSON response containing the FastUI page components.
    """
    return Response(
        FastUI(root=[c.Heading(text="Hello World")]).model_dump_json(
            by_alias=True,
            exclude_none=True,
        ),
        content_type="application/json",
        charset="utf-8",
    )


def root(request: Request) -> Response:
    """Serve the FastUI React app shell, comes last as it matches all paths.

    Returns:
        An HTML page that loads the prebuilt FastUI app.
    """
    return Response(
        prebuilt_html(title="FastUI and Pyramid Example"),
        content_type="text/html",
    )


with Configurator() as config:
    # Routes are matched in registration order, so the catch-all goes last.
    config.add_route("api", "/api/")
    config.add_view(page, route_name="api")
    config.add_route("root", "/*path")
    config.add_view(root, route_name="root")
    app = config.make_wsgi_app()


def main() -> None:
    """Run the example with the standard library WSGI server."""
    with make_server("127.0.0.1", 8000, app) as server:
        print("Serving on http://127.0.0.1:8000")
        server.serve_forever()


if __name__ == "__main__":
    main()
