"""Updated Todo program"""


def add_todo():
    todo = input('Enter a todo: ')
    return todo

def read_file():
    """Reads todo.txt file and returns list of to-dos"""
    todo_list = []
    with open('todo.txt', 'r') as file:
        for line in file:
            todo_list.append(line.strip())
    return todo_list

def write_file(todo_list):
    """Writes todo_list to todo.txt"""
    with open('todo.txt', 'w') as file:
        for todo in todo_list:
            this_todo = todo + '\n'
            file.write(this_todo)

def print_menu():
    """Prints menu and returns choice"""
    selections = ["ADD", "EDIT", "SHOW", "COMPLETE", "EXIT"]
    for i, selection in enumerate(selections, 1):
        print(f" {i} : {selection}")

    option = input("Enter option here: ")

    if option.isdigit():
        return int(option)
    else:
        return option.lower().strip()
    
def print_todo_list(todo_list):
    """Prints todo_list"""
    for i, todo in enumerate(todo_list, 1):
        print( f"{i}: {todo}")

def edit_list(todo_list):
    """Edit or delete items in todo_list"""
    print_todo_list(todo_list)

    while True:
        selection = input("Enter item number to edit: ")
        if selection.isdigit() and (int(selection) <= len(todo_list)):
            selection = int(selection)
            todo_list[selection - 1] = input("What is the new To Do item? ")
            return todo_list

        else:
            print("Invalid selection, please try again.")

def delete_item(todo_list):
    """Delete item from todo_list"""
    print_todo_list(todo_list)

    while True:
        selection = input("Enter item number to delete/complete: ")
        if selection.isdigit() and (int(selection) <= len(todo_list)):
            selection = int(selection)
            todo_list.remove(todo_list[selection - 1])
            return todo_list

        else:
            print("Invalid selection, please try again.")

def save_and_exit(todo_list):
    """Save todo_list to todo.txt and exit program"""
    write_file(todo_list)
    print("Your to-do list has been saved.")
    exit()

def main():
    todo_list = read_file()
    while True:
        options = print_menu()
        if options == 1:
            todo_list.append(add_todo())
        elif options == 2:
            todo_list = edit_list(todo_list)
        elif options == 3:
            print_todo_list(todo_list)
        elif options == 4:
            todo_list = delete_item(todo_list)
        elif options == 5:
            save_and_exit(todo_list)
        else:
            print("Invalid selection, please try again.")
