from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .comment_reaction import CommentReaction
from .post_reaction import PostReaction


class Reaction(Base):
    __tablename__ = "reaction"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    type:Mapped[str] = mapped_column(nullable=False, unique=True)

    comment_reaction: Mapped[list[CommentReaction]] = relationship(back_populates="reaction")
    post_reaction: Mapped[list[PostReaction]] = relationship(back_populates="reaction")
    pass