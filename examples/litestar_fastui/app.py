# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
from __future__ import annotations

from typing import TYPE_CHECKING

from fastui import AnyComponent, prebuilt_html
from fastui import components as c
from litestar import Litestar, MediaType, get

if TYPE_CHECKING:
    from pathlib import Path


@get("/api/", media_type=MediaType.JSON)
async def page() -> list[AnyComponent]:
    return [c.Heading(text="Hello World")]


@get(["/", "/{path:path}"], media_type=MediaType.HTML)
async def root(path: Path | None) -> str:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return prebuilt_html(title="FastUI and Litestar Example")


app = Litestar(route_handlers=[root, page])
