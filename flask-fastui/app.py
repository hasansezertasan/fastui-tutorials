# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from __future__ import annotations

from fastui import FastUI, prebuilt_html
from fastui import components as c
from flask import Flask, Response, jsonify

app = Flask(__name__)


@app.get("/api/")
def page() -> Response:
    return jsonify(FastUI(root=[c.Heading(text="Hello World")]).model_dump())


@app.get("/")
@app.get("/<path:subpath>")
def root() -> str:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return prebuilt_html(title="FastUI and Flask Example")


if __name__ == "__main__":
    app.run(debug=True)
