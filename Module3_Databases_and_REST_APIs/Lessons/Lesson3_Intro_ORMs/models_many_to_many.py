from sqlalchemy import Table, Column, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional
from sqlalchemy_setup import Base, engine

# Association table
user_pet = Table(
    "user_pet",
    Base.metadata,
    Column("user_id", ForeignKey("user_account.id")),
    Column("pet_id", ForeignKey("pets.id")),
)

class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[Optional[str]] = mapped_column(String(200))

    pets: Mapped[List["Pet"]] = relationship(secondary=user_pet, back_populates="owners")

class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    animal: Mapped[str] = mapped_column(String(200))

    owners: Mapped[List["User"]] = relationship(secondary=user_pet, back_populates="pets")

# Create tables
Base.metadata.create_all(engine)
