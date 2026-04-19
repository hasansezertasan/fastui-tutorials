# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "fastapi",
#     "fastui>=0.6.0",
#     "uvicorn",
#     "pydantic>=2.0.0",
# ]
# ///
from __future__ import annotations

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.components.display import DisplayLookup
from fastui.events import PageEvent
from pydantic import BaseModel, Field

FastUI.model_rebuild()

app = FastAPI()

USER_DETAILS_EVENT = "user-details"


class User(BaseModel):
    id: int = Field(title="ID")
    name: str = Field(title="Name")
    role: str = Field(title="Role")


users = [
    User(id=1, name="Alice", role="Admin"),
    User(id=2, name="Bob", role="User"),
    User(id=3, name="Charlie", role="Developer"),
]


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def users_table() -> list[AnyComponent]:
    return [
        c.Page(
            components=[
                c.Heading(text="Users", level=2),
                c.Paragraph(text="Click on a user ID to see their details below."),
                c.Table(
                    data=users,
                    data_model=User,
                    columns=[
                        DisplayLookup(
                            field="id",
                            on_click=PageEvent(
                                name=USER_DETAILS_EVENT,
                                context={"user_id": "{id}"},
                            ),
                        ),
                        DisplayLookup(field="name"),
                        DisplayLookup(field="role"),
                    ],
                ),
                c.Div(
                    components=[
                        c.ServerLoad(
                            path="/api/user-details/{user_id}",
                            load_trigger=PageEvent(name=USER_DETAILS_EVENT),
                            components=[c.Text(text="Select a user to see details...")],
                        ),
                    ],
                    class_name="border-top mt-3 pt-3",
                ),
            ],
        ),
    ]


@app.get(
    "/api/user-details/{user_id}",
    response_model=FastUI,
    response_model_exclude_none=True,
)
def user_details(user_id: int) -> list[AnyComponent]:
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        return [c.Text(text="User not found")]

    return [
        c.Heading(text=f"Details for {user.name}", level=3),
        c.Paragraph(text=f"ID: {user.id}"),
        c.Paragraph(text=f"Role: {user.role}"),
    ]


@app.get("/{path:path}")
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title="FastUI Table ServerLoad Example"))


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
