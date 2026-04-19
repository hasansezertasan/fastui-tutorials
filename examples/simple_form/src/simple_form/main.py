# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
from __future__ import annotations

from typing import Annotated

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.forms import fastui_form
from pydantic import BaseModel, Field

FastUI.model_rebuild()

app = FastAPI()


class BMIForm(BaseModel):
    weight: float = Field(..., title="Weight (kg)")
    height: float = Field(..., title="Height (m)")

    def calculate_bmi(self) -> float:
        return self.weight / (self.height / 100) ** 2


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
    return [
        c.PageTitle(text="BMI Calculator"),
        c.Page(
            components=[
                c.Heading(text="BMI Calculator", level=2),
                c.Paragraph(text="Enter your weight and height to calculate your BMI."),
                c.ModelForm(model=BMIForm, submit_url="/api/calculate"),
            ],
        ),
    ]


@app.post("/api/calculate", response_model=FastUI, response_model_exclude_none=True)
def calculate_bmi_post(
    form: Annotated[BMIForm, fastui_form(BMIForm)],
) -> list[AnyComponent]:
    text = f"Your BMI is {form.calculate_bmi()}"
    return [c.Paragraph(text=text)]


@app.get("/{path:path}")
def root(path: str) -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="Simple Form: BMI Calculator"))
