"""
This is a ToDo list created from the Udemy course:
    The Python Mega Course: Learn Python in 60 Days with 20 Apps
"""
'''TODO created a main function, set the program to call the main function'''

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
        '''TODO add a list of options, ask user to make a selection
           print choices and pass the option back to the main function'''
        print("Would you like to: ADD, EDIT, SHOW, or EXIT? ")
        selections = ["ADD", "EDIT", "SHOW", "COMPLETE", "EXIT"]
        for i, selection in enumerate(selections, 1):
            print(f" {i} : {selection}")
        
        option = input("Enter option here: ")

        if option.isdigit():
            return int(option)
        else:
            return option.lower().strip()

def make_list():
    todo_list = []
    add_more = True

    while add_more:
        todo_list.append(input("What is your to do item? "))
        add_more = get_continue()

    return todo_list
def complete_item(todo_list):
    print_todo(todo_list)
    while True: 
        selection = input("Enter item number to complete: ")
        if selection.isdigit() and (int(selection) <= len(todo_list)):
            selection = int(selection) - 1
            todo_list.remove(todo_list[selection])

            return todo_list

        else:
            print("Invalid selection, please try again.")

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
        case 'add' | 1:
            todo_list = make_list()
        case 'show' | 3:
                print_todo(todo_list)
        case 'edit' | 2:
            todo_list = get_edit_choice(todo_list)
        case 'complete' | 4:
            todo_list = complete_item(todo_list)
        case 'exit' | 5:
            break
        case other:
            print('Invalid option. Please enter "add", "show", "edit", or "exit"')