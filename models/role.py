from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .employee import Employee


class Role(Base):
    __tablename__ = "role"
    id : Mapped[str] = mapped_column( primary_key = True, autoincrement=True)
    name : Mapped[str] = mapped_column(nullable=False)

    employees: Mapped[list[Employee]] = relationship(back_populates="role")
    pass
