from sqlalchemy import Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .comment import Comment
from .comment_reaction import CommentReaction
from .favorite import Favorite
from .post import Post
from .post_reaction import PostReaction
from .role import Role


class Employee(Base):
    __tablename__ = "employee"
    id : Mapped[int] = mapped_column(primary_key=True, auto_increment=True)

    name : Mapped[str] = mapped_column(null=False)
    surname : Mapped[str] = mapped_column(null=False)
    email : Mapped[str] = mapped_column(null=False, unique=True)
    password: Mapped[str] = mapped_column(null=False)
    profile_picture: Mapped[str] = mapped_column()
    birthday: Mapped[Date] = mapped_column()
    phone_number: Mapped[str] = mapped_column()
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))


    favorites: Mapped[list[Favorite]] = relationship(back_populates='employee')
    post: Mapped[list[Post]] = relationship(back_populates='author')
    role: Mapped[Role] = relationship(back_populates='employees')
    comments: Mapped[list[Comment]] = relationship(back_populates='author')
    comment_reaction: Mapped[list[CommentReaction]] = relationship(back_populates="employee")
    post_reaction: Mapped[list[PostReaction]] = relationship(back_populates="employee")
    pass
