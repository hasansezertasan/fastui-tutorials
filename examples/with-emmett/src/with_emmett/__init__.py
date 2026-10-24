# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""FastUI integration example for Emmett."""

from __future__ import annotations

from emmett import App, response
from fastui import FastUI, prebuilt_html
from fastui import components as c
from granian import Granian

FastUI.model_rebuild()

app = App(__name__)


# Emmett strips trailing slashes from request paths, so "/api" also serves "/api/".
@app.route("/api", methods="get")
async def page() -> str:
    """Return the FastUI component tree.

    Returns:
        The page components serialized as JSON.
    """
    response.headers["content-type"] = "application/json"
    return FastUI(root=[c.Heading(text="Hello World")]).model_dump_json(
        exclude_none=True,
    )


@app.route("/", methods="get")
@app.route("/<any:path>", methods="get")
async def root(path: str = "") -> str:
    """Serve the FastUI React app shell, comes last as it matches all paths.

    Returns:
        An HTML page that loads the prebuilt FastUI app.
    """
    response.headers["content-type"] = "text/html"
    return prebuilt_html(title="FastUI and Emmett Example")


def main() -> None:
    """Run the example with Granian, the server Emmett is built for."""
    Granian("with_emmett:app", interface="rsgi", address="127.0.0.1", port=8000).serve()


if __name__ == "__main__":
    main()
