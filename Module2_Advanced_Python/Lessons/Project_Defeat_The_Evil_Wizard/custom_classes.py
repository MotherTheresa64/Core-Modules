from mod2_project_starter_code import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def power_attack(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"{self.name} performs a POWER ATTACK on {opponent.name} for {damage} damage!")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def cast_spell(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f"{self.name} casts a FIREBALL at {opponent.name} for {damage} damage!")

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=20)
        self.evade_next = False

    def quick_shot(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses QUICK SHOT on {opponent.name} for {damage} damage!")

    def evade(self):
        self.evade_next = True
        print(f"{self.name} prepares to EVADE the next attack!")

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=22)
        self.shielded = False

    def holy_strike(self, opponent):
        damage = self.attack_power + 20
        opponent.health -= damage
        print(f"{self.name} uses HOLY STRIKE on {opponent.name} for {damage} damage!")

    def divine_shield(self):
        self.shielded = True
        print(f"{self.name} activates DIVINE SHIELD and will block the next attack!")
