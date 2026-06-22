from sqlalchemy.orm import mapped_column, Mapped, relationship

from .base import Base
from .post_tag import PostTag


class Tag(Base):
    __tablename__ = "tag"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    post_tags: Mapped[list[PostTag]] = relationship(backpopulate='tag')
    pass