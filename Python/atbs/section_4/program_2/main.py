'''
Using what we've learned, lets make do a guess
the number game!

We'll learn about imports here
'''

"""
 
   /$$$$$$                                        
  /$$__  $$                                       
 | $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$
 | $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/
 | $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$ 
 | $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$
 |  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/
  \______/  \______/  \_______/|_______/|_______/ 
                                                  
                                                  
                                                  
 
    /$$     /$$                
   | $$    | $$                
  /$$$$$$  | $$$$$$$   /$$$$$$ 
 |_  $$_/  | $$__  $$ /$$__  $$
   | $$    | $$  \ $$| $$$$$$$$
   | $$ /$$| $$  | $$| $$_____/
   |  $$$$/| $$  | $$|  $$$$$$$
    \___/  |__/  |__/ \_______/
                               
                               
                               
  /$$   /$$                         /$$                          
 | $$$ | $$                        | $$                          
 | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
 | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
 | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
 | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
 | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      
                                                                 
                                                                 
                                                                 
 
"""


import random
name = input("Hello! What is your name? ")

secretNumber = random.randint(1, 20)

print(f"Well, {name}, I am thinking of a number between 1 and 20. Can you guess it in 6 tries?")

# Get guesses from player
for guesses in range(1, 6):
    guess = int(input("Enter your guess: "))
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # If the guess is not too high, or low, must be correct!

if (guess == secretNumber) and (guesses == 1):
    print(f"Great job, {name}, you guessed it in {guesses} try!")
elif guess == secretNumber:
    print(f"Good job, {name}, you guessed it in {guesses} tries!")
else:
    print(f"Good try, but my number was {secretNumber}.")
