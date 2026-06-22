from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base
from .employee import Employee
from .post import Post
from .reaction import Reaction


class PostReaction(Base):
    __tablename__ = 'post_reaction'

    reaction_id: Mapped[int] = mapped_column(ForeignKey('reaction.id'), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), nullable=False)
    employee_id: Mapped[int] = mapped_column(ForeignKey('employee.id'), nullable=False)

    reaction: Mapped[Reaction] = relationship(back_populates='post_reaction')
    post: Mapped[Post] = relationship(back_populates='post_reaction')
    employee: Mapped[Employee] = relationship(back_populates='post_reaction')

    pass