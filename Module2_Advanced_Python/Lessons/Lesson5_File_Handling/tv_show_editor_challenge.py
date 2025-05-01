from tv_show_manager import read_shows, write_show, view

def edit_show(shows):
    view(shows)
    idx = int(input("Which show number do you want to edit? ")) - 1
    if 0 <= idx < len(shows):
        show = shows[idx]
        field = input("Edit 'Platform' or 'Genre'? ").capitalize()
        if field in ['Platform', 'Genre']:
            new_value = input(f"New {field}: ")
            show[field] = new_value
            write_show(shows)
            print(f"{field} updated for {show['Title']}")
        else:
            print("Invalid field.")
    else:
        print("Invalid index.")

def main():
    while True:
        shows = read_shows()
        action = input('''\nEdit Menu
1 - View Shows
2 - Edit a Show
3 - Quit\n''')
        if action == '1':
            view(shows)
        elif action == '2':
            edit_show(shows)
        elif action == '3':
            break

main()
