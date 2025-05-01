def write_foods(foods):
    with open('foods.txt', 'w') as file:
        for food in foods:
            file.write(food + '\n')

def read_foods():
    try:
        with open('foods.txt', 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

def main():
    foods = read_foods()
    while True:
        action = input("1 - Add Food, 2 - View Foods, 3 - Remove Food, 4 - Quit\n")
        if action == '1':
            new_food = input("Enter the name of the food: ")
            foods.append(new_food)
            write_foods(foods)
        elif action == '2':
            print("Your favorite foods:")
            for food in foods:
                print(food)
        elif action == '3':
            for idx, food in enumerate(foods, start=1):
                print(f"{idx}. {food}")
            idx = int(input("Which food to remove? ")) - 1
            if 0 <= idx < len(foods):
                foods.pop(idx)
                write_foods(foods)
        elif action == '4':
            break

main()
