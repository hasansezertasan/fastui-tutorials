# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.events import GoToEvent

app = FastAPI()


def layout(*components: AnyComponent, title: str) -> list[AnyComponent]:
    return [
        c.PageTitle(text=title),
        c.Navbar(
            title="Site Title",
            title_event=GoToEvent(url="/"),
            start_links=[
                c.Link(
                    components=[c.Text(text="About")],
                    on_click=GoToEvent(url="/about"),
                    active="startswith:/about",
                ),
                c.Link(
                    components=[c.Text(text="Contact")],
                    on_click=GoToEvent(url="/contact"),
                    active="startswith:/contact",
                ),
                c.Link(
                    components=[c.Text(text="GitHub")],
                    on_click=GoToEvent(
                        url="https://github.com/hasansezertasan", target="_blank"
                    ),
                ),
            ],
        ),
        c.Page(components=components),
    ]


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
    return layout(c.Text(text="Home Page!"), title="Home Page!")


@app.get("/api/about", response_model=FastUI, response_model_exclude_none=True)
def page_about() -> list[AnyComponent]:
    return layout(c.Text(text="About Page!"), title="About Page!")


@app.get("/api/contact", response_model=FastUI, response_model_exclude_none=True)
def page_contact() -> list[AnyComponent]:
    return layout(c.Text(text="Contact Page!"), title="Contact Page!")


@app.get("/{path:path}")
def root() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="FastUI Navigation"))
