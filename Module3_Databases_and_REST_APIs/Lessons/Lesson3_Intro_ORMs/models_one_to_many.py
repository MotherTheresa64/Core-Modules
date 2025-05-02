from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from sqlalchemy_setup import Base, engine

# User model
class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]] = mapped_column(String(200))

    pets: Mapped[List["Pet"]] = relationship(back_populates="owner", cascade="all, delete-orphan")

# Pet model
class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    animal: Mapped[str] = mapped_column(String(200))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))

    owner: Mapped["User"] = relationship(back_populates="pets")

# Create tables
Base.metadata.create_all(engine)
