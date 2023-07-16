'''
A twist on the "hello world" program of Python

Why the twist? 

print("Hello World!")

The above may be the typical first program for Python,
as it is the easiest program to write that "does" something,
it is also very, very simple.
'''

greetings = ["Hello Wêreld!", "Përshendetje Botë!",
             "Kaixo Mundua!", "Hei maailma!", "Hallo Welt!",
             "Olá Mundo!", "Hello World!"]


print("Hello world, from around the world:")
for greeting in greetings:
    print(greeting)

'''
This programs involves creating a list of strings, printing a
string message to the console, looping through the list, and
printing the stored data in each element
'''
