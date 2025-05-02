from sqlalchemy.orm import Session
from sqlalchemy import select
from models_many_to_many import User, Pet
from sqlalchemy_setup import engine

session = Session(engine)

# Create users and pets
alice = User(name="Alice", email="alice@example.com")
bob = User(name="Bob", email="bob@example.com")
dog = Pet(name="Buddy", animal="Dog")
cat = Pet(name="Whiskers", animal="Cat")

# Assign relationships
alice.pets.append(dog)
bob.pets.append(dog)
bob.pets.append(cat)

# Add to session and commit
session.add_all([alice, bob, dog, cat])
session.commit()

# Query pets owned by Bob
bob_query = select(User).where(User.name == "Bob")
bob_user = session.execute(bob_query).scalars().first()

for pet in bob_user.pets:
    print(f"Bob owns: {pet.name}")

# Query owners of Buddy
dog_query = select(Pet).where(Pet.name == "Buddy")
dog_pet = session.execute(dog_query).scalars().first()

for owner in dog_pet.owners:
    print(f"Buddy is owned by: {owner.name}")
