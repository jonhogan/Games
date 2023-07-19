'''
Lists! We love lists in Python.
Similar to a vector in C++, though not all items/elements
in a list must be the same type.
'''

names = ["Sam", "Lilly", "Erika", "Jane"]

'''
Access individual items in a list

reminder, in programming, we start count at 0
because we're cool like that 
'''

print(names[0])
print(names[3])

# last element of a list
print(names[-1])
print(names[-2])

'''
You can use the print method to print all items in a list
'''

print(names)

'''
Can print a slice of a list
'''

print(names[1:3])

'''
del statement to delete an item
'''

del names[3]
print(names)

'''
Append to add
'''
names.append('Jane')
print(names)

'''
for loops and lists
'''

for name in names:
    print(f"My name is {name}.")


'''
A list of lists
'''

numbers = [[1, 2, 3,], [4, 5, 6,], [7, 8, 9]]

print(numbers)
'''
To access items individual items of a list in a list (like a 2D array)
'''
print(numbers[0][0])
