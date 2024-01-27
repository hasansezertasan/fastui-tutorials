from __future__ import annotations as _annotations

import random
import time

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c
from fastui.events import GoToEvent, PageEvent

app = FastAPI()


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
	title = "Random Number Generator"
	return [
		c.PageTitle(text=title),
		c.Navbar(title=title, title_event=GoToEvent(url="/")),
		c.Page(
			components=[
				c.Heading(text=title),
				c.Div(
					components=[
						c.ServerLoad(
							path="/replace",
							load_trigger=PageEvent(name="replace"),
							components=[
								c.Button(
									text=f"Random: {random.randint(1,100)}",
									on_click=PageEvent(name="replace"),
								),
							],
						),
					],
					class_name="border-top mt-3 pt-1",
				),
			],
		),
	]


@app.get("/api/replace", response_model=FastUI, response_model_exclude_none=True)
async def modal_view() -> list[AnyComponent]:
	time.sleep(0.5)
	return [
		c.ServerLoad(
			path="/replace",
			load_trigger=PageEvent(name="replace"),
			components=[
				c.Button(
					text=f"Random: {random.randint(1,100)}",
					on_click=PageEvent(name="replace"),
				),
			],
		),
	]


@app.get("/{path:path}")
async def html_landing() -> HTMLResponse:
	"""Simple HTML page which serves the React app, comes last as it matches all paths."""
	return HTMLResponse(prebuilt_html(title="FastUI Demo"))
