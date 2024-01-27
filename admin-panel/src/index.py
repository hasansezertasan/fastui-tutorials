from __future__ import annotations as _annotations

from fastapi import APIRouter
from fastui import AnyComponent, FastUI
from fastui import components as c
from fastui.components.display import DisplayLookup, DisplayMode

from src.db import LocalSession, Post, User
from src.schemas import PostView, UserView

from .master import Master

router = APIRouter()


@router.get(
	path="/user",
	response_model=FastUI,
	response_model_exclude_none=True,
)
async def user() -> list[AnyComponent]:
	users = []
	with LocalSession() as session:
		users = session.query(User).all()
		users = [UserView.from_orm(user) for user in users]
	return Master(
		c.Page(
			components=[
				c.Heading(text="Users", level=2),
				c.Table(
					data=users,
					columns=[
						DisplayLookup(field="id", mode=DisplayMode.plain),
						DisplayLookup(field="date_created", mode=DisplayMode.date),
						DisplayLookup(field="date_updated", mode=DisplayMode.date),
						DisplayLookup(field="username", mode=DisplayMode.plain),
						DisplayLookup(field="post_count", mode=DisplayMode.plain),
						# DisplayLookup(field="posts"),
					],
				),
			]
		)
	)


@router.get(
	path="/post",
	response_model=FastUI,
	response_model_exclude_none=True,
)
async def post() -> list[AnyComponent]:
	posts = []
	with LocalSession() as session:
		posts = session.query(Post).all()
		posts = [PostView.from_orm(post) for post in posts]
	return Master(
		c.Page(
			components=[
				c.Heading(text="Posts", level=2),
				c.Table(
					data=posts,
					columns=[
						DisplayLookup(field="id", mode=DisplayMode.plain),
						DisplayLookup(field="date_created", mode=DisplayMode.date),
						DisplayLookup(field="date_updated", mode=DisplayMode.date),
						DisplayLookup(field="title", mode=DisplayMode.plain),
						DisplayLookup(field="content", mode=DisplayMode.plain),
						# DisplayLookup(field="user"),
					],
				),
			]
		)
	)


@router.get("/", response_model=FastUI, response_model_exclude_none=True)
def index() -> list[AnyComponent]:
	return Master(c.Markdown(text="# FastUI Admin Demo"))


@router.get("/{path:path}", status_code=404)
async def not_found():
	# So we don't fall through to the index page
	return {"message": "Not Found"}
