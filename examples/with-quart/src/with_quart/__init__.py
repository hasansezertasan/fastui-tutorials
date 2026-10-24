# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""FastUI integration example for Quart."""

from __future__ import annotations

from fastui import FastUI, prebuilt_html
from fastui import components as c
from quart import Quart, Response

FastUI.model_rebuild()

app = Quart(__name__)


@app.get("/api/")
async def page() -> Response:
    """Return the FastUI component tree.

    Returns:
        A JSON response containing the FastUI page components.
    """
    body = FastUI(root=[c.Heading(text="Hello World")]).model_dump_json(
        exclude_none=True,
    )
    return Response(body, content_type="application/json")


@app.get("/")
@app.get("/<path:path>")
async def root(path: str = "") -> str:
    """Serve the FastUI React app shell, comes last as it matches all paths.

    Returns:
        An HTML page that loads the prebuilt FastUI app.
    """
    return prebuilt_html(title="FastUI and Quart Example")


def main() -> None:
    """Run the example with Quart's development server."""
    app.run(host="127.0.0.1", port=8000, debug=True)


if __name__ == "__main__":
    main()
