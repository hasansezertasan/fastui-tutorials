from dataclasses import dataclass
from typing import Any, Union

from fastui import AnyComponent
from fastui import components as c
from fastui.events import GoToEvent


def Master(
	*components: AnyComponent,
	title: str | None = None,
) -> list[AnyComponent]:
	return [
		c.PageTitle(text=f"FastUI Admin Demo — {title}" if title else "FastUI Admin Demo"),
		c.Navbar(
			title="FastUI Demo",
			title_event=GoToEvent(url="/"),
			links=[
				c.Link(
					components=[c.Text(text="Users")],
					on_click=GoToEvent(url="/user"),
					active="startswith:/user",
				),
				c.Link(
					components=[c.Text(text="Posts")],
					on_click=GoToEvent(url="/post"),
					active="startswith:/post",
				),
			],
		),
		c.Page(
			components=[
				*((c.Heading(text=title),) if title else ()),
				*components,
			],
		),
		c.Footer(
			extra_text="FastUI Admin Demo",
			links=[
				c.Link(
					components=[c.Text(text="Github")],
					on_click=GoToEvent(url="https://github.com/hasansezertasan/FastUI-Admin"),
				),
				c.Link(
					components=[c.Text(text="PyPI")], on_click=GoToEvent(url="https://pypi.org/project/fastui-admin/")
				),
			],
		),
	]


@dataclass
class MasterView:
	title: Union[str, None] = "FastUI Admin"

	def render(self, *components: AnyComponent, title: str | None = None) -> list[AnyComponent]:
		return [
			c.PageTitle(text=self.title),
			c.Navbar(
				title=self.title,
				title_event=GoToEvent(url="/"),
				links=[
					c.Link(
						components=[c.Text(text="Components")],
						on_click=GoToEvent(url="/components"),
						active="startswith:/components",
					),
					c.Link(
						components=[c.Text(text="Tables")],
						on_click=GoToEvent(url="/table/cities"),
						active="startswith:/table",
					),
					c.Link(
						components=[c.Text(text="Forms")],
						on_click=GoToEvent(url="/forms/login"),
						active="startswith:/forms",
					),
				],
			),
			c.Page(
				components=[
					*((c.Heading(text=self.title),) if self.title else ()),
					*components,
				],
			),
		]
