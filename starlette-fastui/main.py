# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from __future__ import annotations

from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Route

app = Starlette()


def page(request: Request) -> JSONResponse:
    return JSONResponse(FastUI(root=[c.Heading(text="Hello World")]).model_dump())


def root(request: Request) -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="FastUI Hello World Example"))


app = Starlette(
    routes=[Route("/", root, methods=["GET"]), Route("/api/", page, methods=["GET"])]
)
