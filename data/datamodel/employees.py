from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from .model_base import SqlAlchemyBase


class Employees(SqlAlchemyBase):
    __tablename__ = 'employees'

    id: Mapped[int] = mapped_column(autoincrement=True, nullable=False)
    employee_name: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
    mail: Mapped[str] = mapped_column(nullable=True)
    phone_number: Mapped[Optional[int]] = mapped_column(nullable=True)
