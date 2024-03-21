# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.forms import fastui_form
from pydantic import BaseModel, Field
from typing_extensions import Annotated

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
async def login_form_post(
    form: Annotated[BMIForm, fastui_form(BMIForm)],
) -> list[AnyComponent]:
    text = f"Your BMI is {form.calculate_bmi()}"
    return [c.Paragraph(text=text)]


@app.get("/{path:path}")
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="BMI Calculator"))
