# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
import typer
from src.db import Base, LocalSession, Post, User, sync_engine

app = typer.Typer(name="Blog Site")


@app.command(help="Create database")
def create_database() -> None:
    """Create database

    Usage:
        python toolbox.py create-database
    """
    Base.metadata.create_all(sync_engine)
    typer.echo("Database created")


@app.command(help="Seed database")
def seed_database() -> None:
    """Seed database

    Usage:
        python toolbox.py seed-database
    """
    users = [
        {
            "username": "admin",
            "password": "admin",
            "posts": [
                {
                    "title": "I am not a robot",
                    "content": "Beep boop beep boop.",
                },
                {
                    "title": "It was a dark and stormy night",
                    "content": "The rain fell in torrents.",
                },
            ],
        },
        {
            "username": "John",
            "password": "Doe",
            "posts": [
                {
                    "title": "Being John Doe",
                    "content": "Being John Doe is not easy.",
                },
                {
                    "title": "Why my dog stole my refrigerator?",
                    "content": "I don't know why, but he did it.",
                },
            ],
        },
        {
            "username": "Jane",
            "password": "Doe",
            "posts": [
                {
                    "title": "Jane Doe",
                    "content": "Jane Doe is a great name.",
                },
                {
                    "title": "Jane Doe and the lost ark",
                    "content": "Jane Doe is a great name.",
                },
            ],
        },
    ]
    with LocalSession() as session:
        for user in users:
            posts = user.pop("posts")
            user_obj = User(**user)
            session.add(user_obj)
            session.commit()
            for post in posts:
                post_obj = Post(**post, user_id=user_obj.id)
                session.add(post_obj)
                session.commit()


if __name__ == "__main__":
    app()
