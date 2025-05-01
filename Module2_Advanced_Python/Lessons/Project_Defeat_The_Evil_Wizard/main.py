from game_actions import create_character, EvilWizard

def battle(player, wizard):
    while player.health > 0 and wizard.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if hasattr(player, "power_attack"):
                player.power_attack(wizard)
            elif hasattr(player, "cast_spell"):
                player.cast_spell(wizard)
            elif hasattr(player, "quick_shot"):
                sub_choice = input("a) Quick Shot\nb) Evade\nChoose: ")
                if sub_choice == 'a':
                    player.quick_shot(wizard)
                else:
                    player.evade()
            elif hasattr(player, "holy_strike"):
                sub_choice = input("a) Holy Strike\nb) Divine Shield\nChoose: ")
                if sub_choice == 'a':
                    player.holy_strike(wizard)
                else:
                    player.divine_shield()
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            print(f"{wizard.name} - Health: {wizard.health}/{wizard.max_health}")
        else:
            print("Invalid input.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated by {wizard.name}!")
        elif wizard.health <= 0:
            print(f"{player.name} has defeated {wizard.name} and saved the realm!")

def main():
    player = create_character()
    wizard = EvilWizard()
    battle(player, wizard)

if __name__ == "__main__":
    main()
