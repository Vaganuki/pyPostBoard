from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from models.base import Base
from models.post import Post
from models.tag import Tag


class PostTag(Base):
    __tablename__ = 'post_tag'

    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey('tag.id'), primary_key=True)

    post : Mapped[Post] = relationship(backpopulate='post_tags')
    tag: Mapped[Tag] = relationship(backpopulate='post_tags')
    pass