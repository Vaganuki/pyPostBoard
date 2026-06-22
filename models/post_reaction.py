from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .employee import Employee
    from .post import Post
    from .reaction import Reaction


class PostReaction(Base):
    __tablename__ = 'post_reaction'


    reaction_id: Mapped[int] = mapped_column(ForeignKey('reaction.id'), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), primary_key=True)
    employee_id: Mapped[int] = mapped_column(ForeignKey('employee.id'), primary_key=True)
    reaction: Mapped[Reaction] = relationship(back_populates='post_reaction')
    post: Mapped[Post] = relationship(back_populates='post_reaction')
    employee: Mapped[Employee] = relationship(back_populates='post_reaction')

    pass