from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import LargeBinary, CheckConstraint, ForeignKey

from .model_base import SqlAlchemyBase


class Dishes(SqlAlchemyBase):
    __tablename__ = 'dishes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    dish_name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    photo: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'), unique=True)

    __table_args__ = (
        CheckConstraint('price > 0', name='check_price_positive'),
    )
