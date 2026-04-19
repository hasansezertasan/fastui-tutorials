# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
from __future__ import annotations

from typing import cast

from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from robyn import Headers, Request, Response, Robyn, jsonify, status_codes


def setup_fastui() -> None:
    """Register FastUI components and rebuild models.

    This ensures that AnyComponent and other FastUI types are correctly
    recognized within the Pydantic models when used with Robyn.
    """
    FastUI.model_rebuild(_types_namespace={"AnyComponent": AnyComponent})


setup_fastui()
app = Robyn(__file__)


@app.get("/api/")  # type: ignore[misc]
def page(request: Request) -> Response:
    return cast(
        Response, jsonify(FastUI(root=[c.Heading(text="Hello World")]).model_dump())
    )


@app.get("/*path")  # type: ignore[misc]
@app.get("/")  # type: ignore[misc]
def root(request: Request) -> Response:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return Response(
        status_code=status_codes.HTTP_200_OK,
        description=prebuilt_html(title="FastUI and Robyn Example"),
        headers=Headers({"Content-Type": "text/html; charset=utf-8"}),
    )


if __name__ == "__main__":
    app.start()
