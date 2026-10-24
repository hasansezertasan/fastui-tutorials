# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""FastUI integration example for Bottle."""

from __future__ import annotations

from bottle import Bottle, response
from fastui import FastUI, prebuilt_html
from fastui import components as c

FastUI.model_rebuild()

app = Bottle()


@app.get("/api/")
def page() -> str:
    """Return the FastUI component tree.

    Returns:
        The page components serialized as JSON.
    """
    response.content_type = "application/json"
    return FastUI(root=[c.Heading(text="Hello World")]).model_dump_json(
        exclude_none=True,
    )


@app.get("/")
@app.get("/<path:path>")
def root(path: str = "") -> str:
    """Serve the FastUI React app shell, comes last as it matches all paths.

    Returns:
        An HTML page that loads the prebuilt FastUI app.
    """
    return prebuilt_html(title="FastUI and Bottle Example")


def main() -> None:
    """Run the example with Bottle's built-in server."""
    app.run(host="127.0.0.1", port=8000, reloader=True)


if __name__ == "__main__":
    main()
