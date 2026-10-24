# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
from __future__ import annotations

import uvicorn
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from litestar import Litestar, MediaType, get
from litestar.plugins.pydantic import PydanticPlugin

FastUI.model_rebuild()


@get("/api/", media_type=MediaType.JSON)
async def page() -> list[AnyComponent]:
    return [c.Heading(text="Hello World")]


@get(["/", "/{path:path}"], media_type=MediaType.HTML)
async def root() -> str:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return prebuilt_html(title="FastUI and Litestar Example")


app = Litestar(
    route_handlers=[root, page],
    # FastUI's frontend reads camelCase keys (onClick, className), so serialize
    # with aliases, and drop unset fields like response_model_exclude_none does.
    plugins=[PydanticPlugin(prefer_alias=True, exclude_none=True)],
)


def main() -> None:
    """Run the example with Uvicorn."""
    uvicorn.run("with_litestar:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
