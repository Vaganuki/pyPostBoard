from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class Comment(Base):
    __tablename__ = "comment"
    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(nullable=False)
    

    pass