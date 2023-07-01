grade = int(input("What is the student's grade? "))

if 90 <= grade:
    print("Student got an A")
elif grade > 79:
    print("Student got a B")
elif grade > 69:
    print("Student got a C")
elif grade > 59:
    print("Student got a D")
else:
    print("Student got an F")
