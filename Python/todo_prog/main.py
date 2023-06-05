"""
This is a ToDo list created from the Udemy course:
    The Python Mega Course: Learn Python in 60 Days with 20 Apps
"""

def get_todo():
    todo = input('Enter a todo: ')
    return todo

todo_list = []
for i in range(3):
    todo_list.append(get_todo())

for todo in todo_list:
    print(todo)