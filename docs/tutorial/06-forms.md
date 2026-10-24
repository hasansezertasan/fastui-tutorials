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
    weight: int = Field(..., gt=0, title="Weight (kg)")
    height: int = Field(..., gt=0, title="Height (cm)")

    def calculate_bmi(self) -> float:
        return self.weight / (self.height / 100) ** 2
```

- Each field becomes an input, and the type picks the kind (`int` and `float` give a number input, `bool` a checkbox, `Enum` a select).
- `title` is the label.
- Constraints such as `gt=0` are validated by Pydantic **on the server**. The error comes back and the React app shows it next to the field.

The fields are `int` on purpose, which is a trap worth knowing.
With FastUI 0.9, a `float` field becomes `<input type="number">` with no `step`, and browsers treat that as `step="1"`, so typing `1.75` is rejected with "The two nearest valid values are 1 and 2" before anything is sent.
Pick units that fit whole numbers (centimetres, not metres), or use a text field and convert yourself.

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
    return [c.Paragraph(text=f"Your BMI is {form.calculate_bmi():.1f}")]
```

`fastui_form(BMIForm)` is a FastAPI dependency that reads the submitted form data and validates it into a `BMIForm`.
If validation fails, FastUI returns errors in a format the React app shows next to the offending fields, and your function never runs.

By default, the components you return replace the form, which is why the result appears in its place.
`ModelForm` has other submit behaviours too: `method="GOTO"` navigates to `submit_url` with the form data as query parameters instead of posting, `submit_on_change=True` submits whenever a field changes, and `submit_trigger` submits when a `PageEvent` fires. The [chatbot example](../../examples/chatgpt/) uses `method="GOTO"`.

## Try it

- Enter `0` for height and see the server-side error.
- Change the result format: the handler uses `:.1f`, so try `:.2f`.
- Add a `bool` field to the model and watch a checkbox appear.

Next: [Tables](07-tables.md).
