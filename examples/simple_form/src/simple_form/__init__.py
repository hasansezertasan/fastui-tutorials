# Copyright (C) 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
from __future__ import annotations

from typing import Annotated

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.forms import fastui_form
from pydantic import BaseModel, Field

FastUI.model_rebuild()

app = FastAPI()


class BMIForm(BaseModel):
    # Whole numbers: FastUI renders float fields as <input type="number"> without
    # a step, so browsers refuse decimals such as 1.75.
    weight: int = Field(..., gt=0, title="Weight (kg)")
    height: int = Field(..., gt=0, title="Height (cm)")

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
    text = f"Your BMI is {form.calculate_bmi():.1f}"
    return [c.Paragraph(text=text)]


@app.get("/{path:path}")
def root(path: str) -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="Simple Form: BMI Calculator"))


def main() -> None:
    """Run the example with Uvicorn."""
    uvicorn.run("simple_form:app", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    main()
