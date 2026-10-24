# 6. Forms

Example: [`examples/simple_form`](../../examples/simple_form/)

```shell
cd examples/simple_form
uv run simple-form
```

This is where FastUI's Pydantic foundation pays off: you describe a form as a model, and FastUI builds the inputs.

## The model is the form

```python
class BMIForm(BaseModel):
    weight: float = Field(..., title="Weight (kg)")
    height: float = Field(..., gt=0, title="Height (m)")

    def calculate_bmi(self) -> float:
        return self.weight / self.height**2
```

- Each field becomes an input, and the type picks the kind (`float` gives a number input, `bool` a checkbox, `Enum` a select).
- `title` is the label.
- Constraints such as `gt=0` become validation rules, checked in the browser and again on the server.

## Showing it

```python
c.ModelForm(model=BMIForm, submit_url="/api/calculate")
```

`ModelForm` renders the model as a form and posts it to `submit_url` on submit.

## Handling the submission

```python
@app.post("/api/calculate", response_model=FastUI, response_model_exclude_none=True)
def calculate_bmi_post(
    form: Annotated[BMIForm, fastui_form(BMIForm)],
) -> list[AnyComponent]:
    return [c.Paragraph(text=f"Your BMI is {form.calculate_bmi()}")]
```

`fastui_form(BMIForm)` is a FastAPI dependency that reads the submitted form data and validates it into a `BMIForm`.
If validation fails, FastUI returns errors in a format the React app shows next to the offending fields, and your function never runs.

By default, the components you return replace the form, which is why the result appears in its place.
`ModelForm` has other submit behaviours too: `method="GOTO"` navigates to `submit_url` with the form data as query parameters instead of posting, `submit_on_change=True` submits whenever a field changes, and `submit_trigger` submits when a `PageEvent` fires. The [chatbot example](../../examples/chatgpt/) uses `method="GOTO"`.

## Try it

- Enter `0` for height and see the server-side error.
- Round the result with an f-string format spec such as `{bmi:.1f}`.
- Add a `bool` field to the model and watch a checkbox appear.

Next: [Tables](07-tables.md).
