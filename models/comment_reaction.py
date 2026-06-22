from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .comment import Comment
    from .employee import Employee
    from .reaction import Reaction


class CommentReaction(Base):
    __tablename__ = 'comment_reaction'

    reaction_id: Mapped[int] = mapped_column(ForeignKey('reaction.id'), primary_key=True)
    comment_id: Mapped[int] = mapped_column(ForeignKey('comment.id'), primary_key=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey('employee.id'), primary_key=True)

    reaction: Mapped[Reaction] = relationship(back_populates='comment_reaction')
    comment: Mapped[Comment] = relationship(back_populates='comment_reaction')
    employee: Mapped[Employee] = relationship(back_populates='comment_reaction')
    pass