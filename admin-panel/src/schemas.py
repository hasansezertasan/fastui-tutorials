import datetime

from pydantic import BaseModel, Field, computed_field
from fastui.components.display import DisplayMode


class ReadMixin(BaseModel):
    id: int = Field(
        title='ID',
        exclude_create=True,
        exclude_edit=True,
    )
    date_created: datetime.datetime = Field(
        title='Date Created',
        description='Date created!',
        mode=DisplayMode.plain,
        exclude_create=True,
        exclude_edit=True,
    )
    date_updated: datetime.datetime = Field(
        title='Date Updated',
        mode=DisplayMode.datetime,
    )


class UserView(ReadMixin):
    username: str = Field(
        title='Username',
        mode=DisplayMode.as_title,
    )
    password: str = Field(
        title='Password',
        exclude_list=True,
    )
    posts: list['PostView'] = Field(
        title='Posts',
        exclude_list=True,
    )

    @computed_field(title="Post Count", alias="post_count")
    def post_count(self) -> int:
        return len(self.posts)

    class Config:
        orm_mode = True
        from_attributes = True


class PostView(ReadMixin):
    title: str = Field(
        title='Title',
        mode=DisplayMode.as_title,
    )
    content: str = Field(
        title='Content',
        mode=DisplayMode.markdown,
    )
    user_id: int = Field(
        title='User ID',
    )

    class Config:
        orm_mode = True
        from_attributes = True