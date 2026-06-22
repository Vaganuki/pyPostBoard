from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

if TYPE_CHECKING:
    from .post import Post
    from .tag import Tag


class PostTag(Base):
    __tablename__ = 'post_tag'

    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey('tag.id'), primary_key=True)

    post : Mapped[Post] = relationship(back_populates='post_tags')
    tag: Mapped[Tag] = relationship(back_populates='post_tags')
    pass