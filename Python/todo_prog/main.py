"""
This is a ToDo list created from the Udemy course:
    The Python Mega Course: Learn Python in 60 Days with 20 Apps
"""

def get_todo():
    todo = input('Enter a todo: ')
    return todo

def get_continue():
    while True:
        choice = input("Do you have more items (yes/no)? ")

        if choice.lower() in ('n', 'no'):
            return False
        elif choice.lower() in ('y', 'yes'):
            return True
        else:
            print('Invalid input')


def print_menu():
        options = input("Would you like to ADD, EDIT, SHOW, or EXIT? ").lower().strip()
        return options.lower().strip()

def make_list():
    todo_list = []
    add_more = True

    while add_more:
        todo_list.append(input("What is your to do item? "))
        add_more = get_continue()

    return todo_list

def print_todo(todo_list):
    for i, todo in enumerate(todo_list, 1):
        print( f"{i}: {todo}")

def edit_list(todo_list, element):
    todo_list[element - 1] = input("What is the new To Do item? ")
    return todo_list

def get_edit_choice(todo_list):
    print_todo(todo_list)
    
    while True: 
        selection = input("Enter item number to edit: ")
        if selection.isdigit() and (int(selection) <= len(todo_list)):
            selection = int(selection)
            todo_list = edit_list(todo_list, selection)

            return todo_list

        else:
            print("Invalid selection, please try again.")
        

todo_list = []
while True:
    options = print_menu()
    match options:
        case 'add':
            todo_list = make_list()
        case 'show':
                print_todo(todo_list)
        case 'edit':
            todo_list = get_edit_choice(todo_list)
        case 'exit':
            break
        case other:
            print('Invalid option. Please enter "add", "show", "edit", or "exit"')