spam = 42       # Global scope, can be called in all functions


def function_lesson():
    eggs = "ham"    # Local scope, can only be called in this function
    print(eggs)
    print(spam)


function_lesson()

print()
print(spam)
print(eggs)
