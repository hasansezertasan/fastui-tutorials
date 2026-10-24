# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""FastUI integration example for Sanic."""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastui import FastUI, prebuilt_html
from fastui import components as c
from sanic import HTTPResponse, Sanic
from sanic.response import html, json

if TYPE_CHECKING:
    from sanic import Request

FastUI.model_rebuild()

app = Sanic("with_sanic")


# Strict slashes keep the catch-all below from swallowing "/api/".
@app.get("/api/", strict_slashes=True)
async def page(request: Request) -> HTTPResponse:
    """Return the FastUI component tree.

    Returns:
        A JSON response containing the FastUI page components.
    """
    return json(
        FastUI(root=[c.Heading(text="Hello World")]).model_dump(
            by_alias=True,
            exclude_none=True,
        ),
    )


@app.get("/", name="root_index")
@app.get("/<path:path>")
async def root(request: Request, path: str = "") -> HTTPResponse:
    """Serve the FastUI React app shell, comes last as it matches all paths.

    Returns:
        An HTML response that loads the prebuilt FastUI app.
    """
    return html(prebuilt_html(title="FastUI and Sanic Example"))


def main() -> None:
    """Run the example with Sanic's development server."""
    app.run(host="127.0.0.1", port=8000, single_process=True)


if __name__ == "__main__":
    main()
