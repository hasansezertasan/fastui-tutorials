# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c

fooapp = FastAPI()


@fooapp.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def foo_page() -> list[AnyComponent]:
    return [c.Heading(text="Sub Application Foo API!")]


@fooapp.get("/{path:path}")
def foo_root() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(
        prebuilt_html(
            title="Sub Application Foo",
            api_root_url="/foo/api",
            api_path_strip="/foo",
        )
    )


barapp = FastAPI()


@barapp.get("/api/v1/", response_model=FastUI, response_model_exclude_none=True)
def bar_page() -> list[AnyComponent]:
    return [c.Heading(text="Sub Application Bar API!")]


@barapp.get("/{path:path}")
def bar_root() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(
        prebuilt_html(
            title="Sub Application Bar",
            api_root_url="/bar/api/v1",
            api_path_strip="/bar",
        )
    )


app = FastAPI()
app.mount("/foo", fooapp)
app.mount("/bar", barapp)
