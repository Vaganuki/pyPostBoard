from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base
from .comment import Comment
from .employee import Employee
from .reaction import Reaction


class CommentReaction(Base):
    __tablename__ = 'comment_reaction'

    reaction_id: Mapped[int] = mapped_column(ForeignKey('reaction.id'), nullable=False)
    comment_id: Mapped[int] = mapped_column(ForeignKey('comment.id'), nullable=False)
    employee_id: Mapped[int] = mapped_column(ForeignKey('employee.id'), nullable=False)

    reaction: Mapped[Reaction] = relationship(back_populates='comment_reaction')
    comment: Mapped[Comment] = relationship(back_populates='comment_reaction')
    employee: Mapped[Employee] = relationship(back_populates='comment_reaction')
    pass