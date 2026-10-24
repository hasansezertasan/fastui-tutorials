# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
from __future__ import annotations

from typing import TYPE_CHECKING

import uvicorn
from fastui import FastUI, prebuilt_html
from fastui import components as c
from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Route

if TYPE_CHECKING:
    from starlette.requests import Request

FastUI.model_rebuild()


def page(request: Request) -> JSONResponse:
    return JSONResponse(
        FastUI(root=[c.Heading(text="Hello World")]).model_dump(
            by_alias=True,
            exclude_none=True,
        ),
    )


def root(request: Request) -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="FastUI and Starlette Example"))


app = Starlette(
    routes=[
        Route("/api/", page, methods=["GET"]),
        Route("/{path:path}", root, methods=["GET"]),
    ],
)


def main() -> None:
    """Run the example with Uvicorn."""
    uvicorn.run("with_starlette:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
