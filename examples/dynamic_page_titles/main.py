# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c

FastUI.model_rebuild()

app = FastAPI()


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
    return [c.PageTitle(text="Updated | FastUI Dynamic Page Titles")]


@app.get("/{path:path}")
def root(path: str) -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="Initial | FastUI Dynamic Page Titles"))
