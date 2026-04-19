# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""FastUI integration example for BlackSheep."""

from __future__ import annotations

import uvicorn
from blacksheep import Application, Response, html
from blacksheep import json as json_response
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c

FastUI.model_rebuild(_types_namespace={"AnyComponent": AnyComponent})


app = Application()


@app.router.get("/api/")
def page() -> Response:
    """Return the FastUI component tree.

    Returns:
        A JSON response containing the FastUI page components.
    """
    return json_response(FastUI(root=[c.Heading(text="Hello World")]).model_dump())


def root() -> Response:
    """Serve the FastUI React app shell.

    Returns:
        An HTML response containing the FastUI prebuilt shell.
    """
    return html(prebuilt_html(title="FastUI and BlackSheep Example"))


app.router.fallback = root


def main() -> None:
    """Run the BlackSheep example with Uvicorn."""
    uvicorn.run("with_blacksheep:app", host="127.0.0.1", port=8000, reload=True)
