# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
"""FastUI integration example for Tornado."""

from __future__ import annotations

import asyncio

import tornado.web
from fastui import FastUI, prebuilt_html
from fastui import components as c

FastUI.model_rebuild()


class PageHandler(tornado.web.RequestHandler):
    """Serve the FastUI component tree."""

    def get(self) -> None:
        """Write the page components as JSON."""
        self.set_header("Content-Type", "application/json")
        self.write(
            FastUI(root=[c.Heading(text="Hello World")]).model_dump_json(
                exclude_none=True,
            ),
        )


class RootHandler(tornado.web.RequestHandler):
    """Serve the FastUI React app shell."""

    def get(self, path: str = "") -> None:
        """Write an HTML page that loads the prebuilt FastUI app."""
        self.write(prebuilt_html(title="FastUI and Tornado Example"))


def make_app() -> tornado.web.Application:
    """Build the Tornado application.

    Returns:
        The application with the API route first and the catch-all last.
    """
    return tornado.web.Application(
        [
            (r"/api/", PageHandler),
            (r"/(.*)", RootHandler),
        ],
    )


app = make_app()


async def serve() -> None:
    """Listen on port 8000 until interrupted."""
    app.listen(8000, address="127.0.0.1")
    print("Serving on http://127.0.0.1:8000")
    await asyncio.Event().wait()


def main() -> None:
    """Run the example with Tornado's server."""
    asyncio.run(serve())


if __name__ == "__main__":
    main()
