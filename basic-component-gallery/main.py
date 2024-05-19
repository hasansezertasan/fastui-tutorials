# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import AnyComponent, FastUI, prebuilt_html
from fastui import components as c

app = FastAPI()


def representation_block(
    type: str,
    description: str,
    input_text: str,
    output_components: list[AnyComponent],
) -> AnyComponent:
    return c.Div(
        components=[
            c.Heading(text=type, level=2),
            c.Paragraph(text=description),
            c.Div(
                components=[
                    c.Div(
                        components=[
                            c.Paragraph(text="Input:"),
                            c.Code(text=input_text, language="python"),
                        ]
                    )
                ],
                class_name="col-6 row",
            ),
            c.Div(
                components=[
                    c.Div(components=[c.Paragraph(text="Output:"), *output_components])
                ],
                class_name="col-6 row",
            ),
        ],
        class_name="row",
    )


@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def page() -> list[AnyComponent]:
    return [
        c.Navbar(title="FastUI Basic Component Gallery"),
        c.Page(
            components=[
                representation_block(
                    type="Text",
                    description="""Text component is a simple text component and has a mandatory text property. It's not rendered as a separate HTML element, it's just a text node""",
                    input_text="""c.Text(text="This is a text component.")""",
                    output_components=[c.Text(text="This is a text component.")],
                ),
                representation_block(
                    type="Paragraph",
                    description="""Like the text component, paragraph component has a mandatory text property. It's rendered as a <p> element in HTML.""",
                    input_text="""c.Paragraph(text="This is a paragraph component.")""",
                    output_components=[
                        c.Paragraph(text="This is a paragraph component.")
                    ],
                ),
                representation_block(
                    type="Heading",
                    description="""Heading component is simply HTML Section Heading element. It has a mandatory text property and an optional level property. The level property is used to determine the size of the heading and it's equivalent to <h1>, <h2>, <h3>, <h4>, <h5>, <h6> in HTML.""",
                    input_text="""c.Heading(text='Heading', level=2),\nc.Heading(text='This is an H3', level=3),\nc.Heading(text='This is an H4', level=4)""",
                    output_components=[
                        c.Heading(text="Heading", level=2),
                        c.Heading(text="This is an H3", level=3),
                        c.Heading(text="This is an H4", level=4),
                    ],
                ),
                representation_block(
                    type="Code",
                    description="""Code component can be used to display code snippets. It has a mandatory text property and an optional language property. The language property is used to determine the syntax highlighting.""",
                    input_text="""c.Code(text="print('Hello, World!')", language='python')""",
                    output_components=[
                        c.Code(text="print('Hello, World!')", language="python")
                    ],
                ),
                representation_block(
                    type="Iframe",
                    description="""Iframe component can be used to embed external content. It has a mandatory src property and optional width and height properties.""",
                    input_text="""c.Iframe(src='https://pydantic.dev', width='100%', height=400)""",
                    output_components=[
                        c.Iframe(src="https://pydantic.dev", width="100%", height=400)
                    ],
                ),
                representation_block(
                    type="Image",
                    description="""Image component can be used to display images. It has a mandatory src property and optional alt, width, height, loading, referrer_policy, loading, on_click, and class_name properties. It's equivalent to <img> element in HTML.""",
                    input_text="""c.Image(src='https://avatars.githubusercontent.com/u/110818415', width=200, height=200)""",
                    output_components=[
                        c.Image(
                            src="https://avatars.githubusercontent.com/u/110818415",
                            width=200,
                            height=200,
                        )
                    ],
                ),
                representation_block(
                    type="Spinner",
                    description="""Spinner component can be used to display a spinner while waiting for content to load. It has a mandatory text property. It also used automatically while loading server content.""",
                    input_text="""c.Spinner(text='Content incoming...')""",
                    output_components=[
                        c.Spinner(text="Content incoming..."),
                    ],
                ),
                representation_block(
                    type="Button",
                    description="""Button component can be used to create buttons. It has a mandatory text property and optional, html_type, named_style, on_click, and class_name properties.""",
                    input_text="""c.Button(text='Primary Button', named_style='primary', class_name='+ ms-2'),\nc.Button(text='Secondary Button', named_style='secondary', class_name='+ ms-2'),\nc.Button(text='Warning Button', named_style='warning', class_name='+ ms-2')""",
                    output_components=[
                        c.Button(
                            text="Primary Button",
                            named_style="primary",
                            class_name="+ ms-2",
                        ),
                        c.Button(
                            text="Secondary Button",
                            named_style="secondary",
                            class_name="+ ms-2",
                        ),
                        c.Button(
                            text="Warning Button",
                            named_style="warning",
                            class_name="+ ms-2",
                        ),
                    ],
                ),
                representation_block(
                    type="Link",
                    description="""Link component can be used to create links. It has a mandatory components property and optional, on_click, mode, active, locked, and class_name properties. The components property is a list of components that will be rendered inside the link.""",
                    input_text="""c.Text(text="This is a link (even though it's not working)!")""",
                    output_components=[
                        c.Text(text="This is a link (even though it's not working)!")
                    ],
                ),
                representation_block(
                    type="LinkList",
                    description="""LinkList component can be used to create a list of links. It has a mandatory links property and optional, mode and class_name properties. The links property is a list of Link components.""",
                    input_text="""c.LinkList(links=[c.Link(components=[c.Text(text="Link A")]), c.Link(components=[c.Text(text="Link B")])""",
                    output_components=[
                        c.LinkList(
                            links=[
                                c.Link(components=[c.Text(text="Link A")]),
                                c.Link(components=[c.Text(text="Link B")]),
                            ],
                        ),
                    ],
                ),
            ]
        ),
    ]


@app.get("/{path:path}")
def root() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="FastUI Basic Component Gallery"))
