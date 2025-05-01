# Writing a list to file
flowers = ["Wysteria", "Sunflowers", "Orchids", "Marigolds"]
with open('garden.txt', 'w') as file:
    for flower in flowers:
        file.write(flower + '\n')

# Reading it back
with open('garden.txt', 'r') as file:
    garden = [line.strip() for line in file]
print("Garden list:", garden)

# Writing a dictionary to file
clubs = {
    'Driver': 'Cobra',
    'Irons': 'Sirixion',
    'Hybrid': 'Callaway',
    'Putter': 'Ping'
}
with open('golf_bag.txt', 'w') as file:
    for club, brand in clubs.items():
        file.write(f"{club}: {brand}\n")

# Reading dictionary from file
golf_clubs = {}
with open('golf_bag.txt', 'r') as file:
    for line in file:
        key, val = line.strip().split(': ')
        golf_clubs[key] = val
print("Golf clubs:", golf_clubs)
