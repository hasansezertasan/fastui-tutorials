# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from dataclasses import dataclass
from typing import Union

from fastui import _PREBUILT_CDN_URL, AnyComponent  # noqa: PLC2701
from fastui import components as c
from fastui.events import GoToEvent

base_template: str = """\
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <script type="module" crossorigin src="{cdn_url}/index.js"></script>
    <link rel="stylesheet" crossorigin href="{cdn_url}/index.css">
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
"""


@dataclass
class MasterView:
    title: Union[str, None] = "FastUI Admin"

    def base(self) -> str:
        return base_template.format(title=self.title, cdn_url=_PREBUILT_CDN_URL)

    def render(
        self, *components: AnyComponent, title: str | None = None
    ) -> list[AnyComponent]:
        title = title or self.title
        return [
            c.PageTitle(text=title),
            c.Navbar(
                title=title,
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
                    *((c.Heading(text=title),) if title else ()),
                    *components,
                ],
            ),
        ]
