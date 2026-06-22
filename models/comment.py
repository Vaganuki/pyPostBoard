from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base
from .comment_reaction import CommentReaction
from .employee import Employee
from .post import Post


class Comment(Base):
    __tablename__ = "comment"
    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(nullable=False)
    employee_id: Mapped[int] = mapped_column(ForeignKey("employee.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"), nullable=False)

    author: Mapped[Employee] = relationship(back_populates="comments")
    post: Mapped[Post] = relationship(back_populates="comments")
    comment_reaction: Mapped[list[CommentReaction]] = relationship(back_populates="comment")
    pass