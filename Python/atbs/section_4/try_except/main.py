def div42(x):
    try:

        print(42 / x)
    except ZeroDivisionError:
        print("Error: You tried to divide by Zero")


div42(3)
div42(0)


'''
Try and Except can also be used for data validation
'''

while True:
    try:
        x = int(input('Enter a number: '))
        break
    except:
        print("That is not a number")

'''
Will not break out of the while loop until the a number is entered
'''
