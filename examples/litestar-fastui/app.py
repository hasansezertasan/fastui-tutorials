# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from fastui import AnyComponent, prebuilt_html
from fastui import components as c
from litestar import Litestar, MediaType, get


@get("/api/", media_type=MediaType.JSON)
async def page() -> List[AnyComponent]:
    return [c.Heading(text="Hello World")]


@get(["/", "/{path:path}"], media_type=MediaType.HTML)
async def root(path: Optional[Path]) -> str:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return prebuilt_html(title="FastUI and Litestar Example")


app = Litestar(route_handlers=[root, page])
