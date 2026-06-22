from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Post(Base):
    __tablename__ = "post"
    id : Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column()
    pass