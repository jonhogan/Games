MAX_LINES = 3

def deposit():
    # Deposit money into the machine
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number.')
    return amount

def get_number_of_lines():
    # get the number of lines to play
    while True:
        lines = input("How many lines would you like to play? ")
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
                break
            else:
                print('You must enter a number between 1 and', MAX_LINES)

def main():
    balance = deposit()
    plays = get_number_of_lines()
    print('You have $', balance, 'and are playing', plays, 'lines.')


main()
