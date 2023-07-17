'''
An introduction to functions in Python

The main goal of a function is to clean up a program,
and avoid writing code more than once.
'''


'''
Let's write a function that will return the powers of a
number
'''


def powers(x):

    for i in range(1, 11):
        x_power = 1
        for j in range(i):
            x_power = x_power * x
        print(f"{x} to the power of {i} is {x_power}")

    print()


'''
Now, we can find upto the 10th power of multiple number without
having the write the algorithm again
'''

# powers(1)
# powers(2)
# powers(3)
# powers(4)


'''
You can also call functions inside loops, making the above code even
more concise
'''

for i in range(5):
    powers(i)
