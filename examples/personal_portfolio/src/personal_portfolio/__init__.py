# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
from __future__ import annotations

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.events import GoToEvent

FastUI.model_rebuild()

app = FastAPI()


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
    return [
        c.PageTitle(text="Hasan Sezer Taşan | Software Developer"),
        c.Page(
            components=[
                c.Image(
                    src="https://github.com/hasansezertasan.png",
                    alt="Profile picture of Hasan Sezer Taşan",
                    width=150,
                    height=150,
                ),
                c.Heading(text="Hasan Sezer Taşan", level=1),
                c.Text(text="Software Developer"),
                c.Paragraph(
                    text="I build small web applications with Python, "
                    "exploring FastAPI and FastUI, and share what I learn.",
                ),
                c.LinkList(
                    links=[
                        c.Link(
                            components=[c.Text(text="GitHub")],
                            on_click=GoToEvent(
                                url="https://github.com/hasansezertasan",
                            ),
                        ),
                        c.Link(
                            components=[c.Text(text="Email")],
                            on_click=GoToEvent(
                                url="mailto:hasansezertasan@gmail.com",
                            ),
                        ),
                        c.Link(
                            components=[c.Text(text="FastUI Tutorials")],
                            on_click=GoToEvent(
                                url="https://github.com/hasansezertasan/fastui-tutorials",
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ]


@app.get("/{path:path}")
def root(path: str) -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="Hasan Sezer Taşan | Software Developer"))


def main() -> None:
    """Run the example with Uvicorn."""
    uvicorn.run("personal_portfolio:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
