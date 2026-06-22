from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .favorite import Favorite


class Post(Base):
    __tablename__ = "post"
    id : Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column()

    favorite: Mapped[Favorite] = relationship(back_populates='post')
    pass