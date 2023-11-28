from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from base import Base

class Apples(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    mass: Mapped[int] = mapped_column(Integer, nullable=False)
    sort: Mapped[str] = mapped_column(String, nullable=False)
    time_of_harvest: Mapped[str] = mapped_column(DateTime, nullable=False)
