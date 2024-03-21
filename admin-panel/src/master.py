# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from __future__ import annotations as _annotations

from fastui import AnyComponent
from fastui import components as c
from fastui.events import GoToEvent


def master(
    *components: AnyComponent,
    title: str | None = None,
) -> list[AnyComponent]:
    return [
        c.PageTitle(
            text=f"FastUI Admin Demo — {title}" if title else "FastUI Admin Demo"
        ),
        c.Navbar(
            title="FastUI Demo",
            title_event=GoToEvent(url="/"),
            links=[
                c.Link(
                    components=[c.Text(text="Users")],
                    on_click=GoToEvent(url="/user"),
                    active="startswith:/user",
                ),
                c.Link(
                    components=[c.Text(text="Posts")],
                    on_click=GoToEvent(url="/post"),
                    active="startswith:/post",
                ),
            ],
        ),
        c.Page(
            components=[
                *((c.Heading(text=title),) if title else ()),
                *components,
            ],
        ),
        c.Footer(
            extra_text="FastUI Admin Demo",
            links=[
                c.Link(
                    components=[c.Text(text="Github")],
                    on_click=GoToEvent(
                        url="https://github.com/hasansezertasan/FastUI-Admin"
                    ),
                ),
                c.Link(
                    components=[c.Text(text="PyPI")],
                    on_click=GoToEvent(url="https://pypi.org/project/fastui-admin/"),
                ),
            ],
        ),
    ]
