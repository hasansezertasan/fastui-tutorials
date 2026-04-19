# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "fastapi",
#     "fastui==0.7.0",
#     "uvicorn",
# ]
# ///
from __future__ import annotations

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c

FastUI.model_rebuild()

app = FastAPI()


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
    # We are returning a list of components
    # We can return any number of components in a list
    return [c.Heading(text="Hello World")]


@app.get("/{path:path}")
def root() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="FastUI Hello World Example"))


if __name__ == "__main__":
    # Run the app with uvicorn
    uvicorn.run("main:app")
