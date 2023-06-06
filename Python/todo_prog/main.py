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

def make_list():
    todo_list = []

    choice = True
    while choice:
        todo_list.append(get_todo())
        choice = get_continue()

    return todo_list


todo_list = make_list() 
for todo in todo_list:
    print(todo)