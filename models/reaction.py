from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Reaction(Base):
    __tablename__ = "reaction"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    type:Mapped[str] = mapped_column(nullable=False, unique=True)
    pass