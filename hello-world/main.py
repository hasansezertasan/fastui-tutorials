from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.events import GoToEvent

app = FastAPI()


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
	return [
		c.PageTitle(text="Title: Hello World!"),
		c.Navbar(
			title="Navbar Title: Hello World!",
			title_event=GoToEvent(url="/"),
		),
		c.Page(
			components=[
				c.Heading(text="H1 Header: Hello World"),
				c.Paragraph(text="Paragraph: This is a simple demo of FastUI."),
			],
		),
	]


@app.get("/{path:path}")
async def html_landing() -> HTMLResponse:
	"""Simple HTML page which serves the React app, comes last as it matches all paths."""
	return HTMLResponse(prebuilt_html(title="FastUI Demo"))
