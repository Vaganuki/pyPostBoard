from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base
from .employee import Employee
from .post import Post


class Favorite(Base):
    table_name = 'favorite'

    employee_id : Mapped[int] = mapped_column(ForeignKey('employee.id'), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'), primary_key=True)

    employee: Mapped[Employee] = relationship(back_populates='favorites')
    post: Mapped[Post] = relationship(back_populates='favorite')

    pass