import datetime
from typing import List

from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    relationship,
    sessionmaker,
)

async_engine = create_async_engine(
    url="sqlite+aiosqlite:///db.sqlite3",
    connect_args={"check_same_thread": False},
    echo=False,
)
AsyncLocalSession = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
    autocommit=False,
)
sync_engine = create_engine(
    url="sqlite:///db.sqlite3",
    connect_args={"check_same_thread": False},
    echo=False,
)
LocalSession = sessionmaker(
    bind=sync_engine,
    class_=Session,
    autoflush=False,
    autocommit=False,
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Mixin:
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        index=True,
    )
    date_created: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow,
    )
    date_updated: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )


class User(Base, Mixin):
    __tablename__ = "user"
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    posts: Mapped[List["Post"]] = relationship(back_populates="user")


class Post(Base, Mixin):
    __tablename__ = "post"
    title: Mapped[str]
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="posts")
