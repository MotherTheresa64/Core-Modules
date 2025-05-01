import re

def write_show(shows):
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")

def read_shows():
    shows = []
    try:
        with open('shows_list.txt', 'r') as file:
            for line in file:
                data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
                if data:
                    shows.append({
                        'Title': data.group(1),
                        'Platform': data.group(2),
                        'Genre': data.group(3).strip()
                    })
    except FileNotFoundError:
        pass
    return shows

def add_show(shows):
    title = input("Title? ")
    platform = input("Platform? ")
    genre = input("Genre? ")
    shows.append({'Title': title, 'Platform': platform, 'Genre': genre})
    write_show(shows)

def view(shows):
    print("\nTV Show List:")
    print("------------------")
    for idx, show in enumerate(shows):
        a_or_an = 'an' if show['Genre'][0].lower() in 'aeiou' else 'a'
        print(f"{idx + 1}.) {show['Title']} is {a_or_an} {show['Genre']} show on {show['Platform']}")

def remove_show(shows):
    view(shows)
    idx = int(input("\nSelect a number to remove: ")) - 1
    if 0 <= idx < len(shows):
        removed = shows.pop(idx)
        print(f"{removed['Title']} removed.")
        write_show(shows)

def main():
    while True:
        shows = read_shows()
        action = input('''\nOptions
1 - Add a TV Show
2 - Remove a TV Show
3 - View List
4 - Quit\n''')
        if action == '1':
            add_show(shows)
        elif action == '2':
            remove_show(shows)
        elif action == '3':
            view(shows)
        elif action == '4':
            print("Goodbye!")
            break

main()
