# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from __future__ import annotations

from typing import List

from fastui import AnyComponent, prebuilt_html
from fastui import components as c
from litestar import Litestar, MediaType, get


@get("/api/", media_type=MediaType.JSON)
def page() -> List[AnyComponent]:
    return [c.Heading(text="Hello World")]


@get("/", media_type=MediaType.HTML)
def root() -> str:
    return prebuilt_html(title="FastUI and Flask Example")


app = Litestar(route_handlers=[root, page])
