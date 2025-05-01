class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"{self.name} attacks with basic strike!")


class Warrior(Character):
    def __init__(self, name, hp, armor):
        super().__init__(name, hp)
        self.armor = armor

    def defend(self):
        print(f"{self.name} blocks with {self.armor} armor!")


class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def cast_spell(self):
        print(f"{self.name} casts a fireball!")


warrior = Warrior("Aragorn", 100, "Steel")
mage = Mage("Gandalf", 80, 100)

warrior.attack()
warrior.defend()

mage.attack()
mage.cast_spell()
