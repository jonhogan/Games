'''
Flow control in Python

We will start with If, Else, Elif statements
'''

# Example of an if statement
name = 'Alice'

if name == 'Alice':
    print(f"Hello, {name}.")
print("Done")

'''
Example of an if/else statement


The following code will ask for a password, and either grant or deny access.
It will only ask once.
'''
password = input("Enter the password: ")
if password == 'Swordfish':
    print('Access granted!')
else:
    print('Invalid password')


'''
The following code will ask for a password, and either grant or deny access.
An improvement on the previous code, as it will allow multiple attempts.

We will ask the user to enter a password, increment a counter then control
the flow of the program based upon entering the correct password, or too many
failed attempts.
'''

count = 0
while True:  # infinite loop (we will see how to get out of it below)
    password = input("Enter the password: ")
    count += 1
    if password == 'Swordfish':
        print('Access granted!')
        break  # This is how we exit the infinite loop
    elif count >= 3:
        print('Too many failed attempts: ACCESS DENIED')
        break
    else:
        print('Invalid password, please try again')

'''
We used a while loop above, let's look more into while loops

A while loop will run until a condition is false, lets rewrite the above code to make use of that
'''

count = 0
while count < 3:
    password = input("Enter the password: ")
    count += 1
    if password == 'Swordfish':
        print('Access granted!')
        break  # This is how we exit the infinite loop
    elif count >= 3:  # This works as the count is incremented at the top of the while loop
        print('Too many failed attempts: ACCESS DENIED')
        # Able to remove the break statement here, since this while loop will terminate at
        # the end of this iteration
    else:
        print('Invalid password, please try again')
