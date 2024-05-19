# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from __future__ import annotations

from typing import List

from fastui import AnyComponent, prebuilt_html
from fastui import components as c
from flask import Flask
from render_response import render_response

app = Flask(__name__)


@app.get("/api/")
def page() -> List[AnyComponent]:
    return render_response([c.Heading(text="Hello World")])


@app.get("/")
def root() -> str:
    return prebuilt_html(title="FastUI and Flask Example")


if __name__ == "__main__":
    app.run(debug=True)
