name = input("What is your name? ")

match name

    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor!")
    case "Luna":
        print("Ravenclaw!")
    case "Draco":
        print("Slytherin!")
    case "Cedric":
        print("Hufflepuff!")
    case _:
        print("Not a Hogwarts' student.")
