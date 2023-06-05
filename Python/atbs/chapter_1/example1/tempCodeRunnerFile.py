"""
Math operations in python
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
print (2 + 3 * 6)
print ((2 + 3) * 6)
print (48565878 * 578453)
print (2 ** 8)
print (23 / 7)
print (23 // 7)
print (23 % 7)
print (2 + 2)
print ((5 - 1) * ((7 + 1) / (3 - 1)))

"""
Data type               |           Examples                          |   Description
Integers                |   -2, -1, 0, 1, 2, 3, 4, 5                  |   Whole numbers
Floating-point numbers  |   -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25   |   Numbers with a decimal point
Strings                 |   'a', 'aa', 'aaa', 'Hello!', '11 cats'     |   Ordered sequence of characters
"""

# You can check the data type of a value by using the type() function
print (type(2))
print (type(42.0))
print (type('Hello World!'))
