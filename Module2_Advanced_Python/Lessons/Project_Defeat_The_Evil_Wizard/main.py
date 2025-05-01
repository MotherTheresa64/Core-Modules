from custom_classes import Warrior, Mage, Archer, Paladin, EvilWizard
from game_actions import use_special, use_defense

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if choice == '1':
        return Warrior(name)
    elif choice == '2':
        return Mage(name)
    elif choice == '3':
        return Archer(name)
    elif choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while player.health > 0 and wizard.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. Use Defensive Ability")
        print("5. View Stats")

        action = input("Choose an action: ")

        if action == '1':
            player.attack(wizard)
        elif action == '2':
            use_special(player, wizard)
        elif action == '3':
            player.heal()
        elif action == '4':
            use_defense(player)
        elif action == '5':
            player.display_stats()
        else:
            print("Invalid choice.")

        if wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()
            if hasattr(player, 'shield_active') and player.shield_active:
                print(f"{player.name}'s Divine Shield blocked the attack!")
                player.shield_active = False
            else:
                wizard.attack(player)

    if player.health <= 0:
        print(f"{player.name} was defeated by the Evil Wizard!")
    elif wizard.health <= 0:
        print(f"{player.name} has defeated the Evil Wizard!")

def main():
    player = create_character()
    wizard = EvilWizard()
    battle(player, wizard)

if __name__ == "__main__":
    main()
