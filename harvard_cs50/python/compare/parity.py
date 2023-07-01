def is_even(n):
    return n % 2 == 0


def main():
    number = int(input("Enter a number: "))
    if is_even(number):
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")


if __name__ == "__main__":
    main()
