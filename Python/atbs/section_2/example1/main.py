import random

"""
Math operations in Python
"""

"""
Highest to lowest precedence
Operators  |   Operation    |   Example    |   Result
**         | Exponentiation |    2 ** 3    |      8
%          | Modulus        |    22 % 8    |      6
//         | Integer division | 22 // 8    |      2
/          | Division       |    22 / 8    |      2.75
*          | Multiplication |    3 * 5     |      15
-          | Subtraction    |    5 - 2     |      3
+          | Addition       |    2 + 2     |      4
"""

# All of these can be done in the python shell
# you do not need to use the print function in the shell
print(2 + 3 * 6)
print((2 + 3) * 6)
print(48565878 * 578453)
print(2 ** 8)
print(23 / 7)
print(23 // 7)
print(23 % 7)
print(2 + 2)
print((5 - 1) * ((7 + 1) / (3 - 1)))

"""
Data types in Python
"""

"""
Data type               |           Examples                          |   Description
Integers                |   -2, -1, 0, 1, 2, 3, 4, 5                  |   Whole numbers
Floating-point numbers  |   -1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25    |   Numbers with a decimal point
Strings                 |   'a', 'aa', 'aaa', 'Hello!', '11 cats'     |   Ordered sequence of characters
Boolean values          |   True, False                               |   True and False
The None type           |   None                                      |   Represents the absence of a value
Tuple                   |   ('Hello', 'World')                        |   Ordered sequence of values of other data types
List                    |   ['Hello', 'World']                        |   Ordered sequence of values of other data types
Dictionary              |   {'name': 'John', 'age': 42}               |   Unordered collection of key-value pairs
"""

# You can check the data type of a value by using the type() function
print(type(2))
print(type(42.0))
print(type('Hello World!'))
print(type(True))

"""
Variables in Python

Variables are like boxes that store data.

x = True        This is a boolean, x will always equal True
x = y > z       This is also a boolean, x will be True only if the value of y is greater than z
x = 1           This is an integer, Variables can store all data types

Python does not use static types. In a language such as C++, the above would not be used, instead the following:

int x = 1;
bool y = False;
bool z = a < b;

Dynamic typing in Python means you could use the same variable name for multiple types of data, but the previously
stored data would be over written
"""

x = 1
print(f'The {type(x)} value of "x" is {x}.')
y = random.randint(0, 100)
z = random.randint(0, 100)

x = y > z

print(f'The {type(x)} value of "x" is {x}. The value of "y" is {y}, and the value of "z" is {z}, and the operation stored in x is "y > z".')

"""
First x was an integer value, now x is an boolean
"""
