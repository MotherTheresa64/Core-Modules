from custom_classes import Warrior, Mage, Archer, Paladin

class EvilWizard:
    def __init__(self, name="The Dark Wizard"):
        self.name = name
        self.health = 150
        self.max_health = 150
        self.attack_power = 15

    def attack(self, player):
        damage = self.attack_power
        if hasattr(player, "evade_next") and player.evade_next:
            print(f"{player.name} dodges the attack!")
            player.evade_next = False
            return
        if hasattr(player, "shielded") and player.shielded:
            print(f"{player.name}'s DIVINE SHIELD blocks the attack!")
            player.shielded = False
            return
        player.health -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage!")

    def regenerate(self):
        regen = 5
        self.health = min(self.health + regen, self.max_health)
        print(f"{self.name} regenerates {regen} health! Current health: {self.health}/{self.max_health}")

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
