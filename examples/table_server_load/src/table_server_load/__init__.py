# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
from __future__ import annotations

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.components.display import DisplayLookup
from fastui.events import GoToEvent
from pydantic import BaseModel, Field

FastUI.model_rebuild()

app = FastAPI()


class User(BaseModel):
    id: int = Field(title="ID")
    name: str = Field(title="Name")
    role: str = Field(title="Role")


users = [
    User(id=1, name="Alice", role="Admin"),
    User(id=2, name="Bob", role="User"),
    User(id=3, name="Charlie", role="Developer"),
]


def back_link() -> AnyComponent:
    return c.Link(
        components=[c.Text(text="Back to users")],
        on_click=GoToEvent(url="/"),
    )


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def users_table() -> list[AnyComponent]:
    return [
        c.PageTitle(text="Users"),
        c.Page(
            components=[
                c.Heading(text="Users", level=2),
                c.Paragraph(text="Click on a user ID to see their details."),
                c.Table(
                    data=users,
                    data_model=User,
                    columns=[
                        # "{id}" is replaced with the clicked row's id
                        DisplayLookup(field="id", on_click=GoToEvent(url="/user/{id}")),
                        DisplayLookup(field="name"),
                        DisplayLookup(field="role"),
                    ],
                ),
            ],
        ),
    ]


@app.get("/api/user/{user_id}", response_model=FastUI, response_model_exclude_none=True)
def user_details(user_id: int) -> list[AnyComponent]:
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        return [
            c.Page(components=[c.Heading(text="User not found", level=2), back_link()]),
        ]

    return [
        c.PageTitle(text=f"Details for {user.name}"),
        c.Page(
            components=[
                c.Heading(text=f"Details for {user.name}", level=2),
                c.Paragraph(text=f"ID: {user.id}"),
                c.Paragraph(text=f"Role: {user.role}"),
                back_link(),
            ],
        ),
    ]


@app.get("/{path:path}")
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title="FastUI Table Example"))


def main() -> None:
    """Run the example with Uvicorn."""
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
