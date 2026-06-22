from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from .comment import Comment
    from .employee import Employee
    from .favorite import Favorite
    from .post_reaction import PostReaction
    from .post_tag import PostTag


class Post(Base):
    __tablename__ = "post"
    id : Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column()
    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"), nullable=False)

    favorite: Mapped[list[Favorite]] = relationship(back_populates='post')
    post_tags: Mapped[list[PostTag]] = relationship(back_populates='post')
    author: Mapped[Employee] = relationship(back_populates='post')
    comments: Mapped[list[Comment]] = relationship(back_populates='post')
    post_reaction: Mapped[list[PostReaction]] = relationship(back_populates="post")
    pass