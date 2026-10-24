# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""FastUI integration example for Falcon."""

from __future__ import annotations

from typing import TYPE_CHECKING
from wsgiref.simple_server import make_server

import falcon
from fastui import FastUI, prebuilt_html
from fastui import components as c

if TYPE_CHECKING:
    from falcon import Request, Response

FastUI.model_rebuild()


class PageResource:
    """Serve the FastUI component tree."""

    def on_get(self, req: Request, resp: Response) -> None:
        """Write the page components as JSON."""
        resp.content_type = falcon.MEDIA_JSON
        resp.text = FastUI(root=[c.Heading(text="Hello World")]).model_dump_json(
            exclude_none=True,
        )


def root(req: Request, resp: Response, **kwargs: str) -> None:
    """Serve the FastUI React app shell, comes last as it matches all paths."""
    resp.content_type = falcon.MEDIA_HTML
    resp.text = prebuilt_html(title="FastUI and Falcon Example")


app = falcon.App()
app.add_route("/api/", PageResource())
# Sinks only run when no route matches, so the catch-all cannot shadow /api/.
app.add_sink(root, prefix="/")


def main() -> None:
    """Run the example with the standard library WSGI server."""
    with make_server("127.0.0.1", 8000, app) as server:
        print("Serving on http://127.0.0.1:8000")
        server.serve_forever()


if __name__ == "__main__":
    main()
