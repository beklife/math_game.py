from random import randint

def start_game():
    print("\nWelcome to Math Practice")
    print("Here you can practice your addition, subtraction and multiplication skills.")
    print("Which would you like to do?")
    print("A - addition")
    print("B - subtraction")
    print("C - multiplication")
    print("D - Exit Game\n")
    choice = input("> ")

    if choice == "A":
        addition()
    elif choice == "B":
        substraction()
    elif choice == "C":
        multiplication()
    elif choice == "D":
        return None
    else:
        print("That's not one of the choices! Try again.\n")
        start_game()

def addition():
    num1 = randint(0, 100)
    num2 = randint(0, 100)

    print(f"What is {num1} + {num2} ?\n")

    choice = input("> ")

    if int(choice) == num1 + num2:
        print("Correct! Nice job! Keep on playing!\n")
        start_game()
    else:
        print(f"Incorrect...the answer is {num1+num2} !\n")
        start_game()


def substraction():
    num1 = randint(0, 100)
    num2 = randint(0, 100)

    print(f"What is {num1} - {num2} ?\n")

    choice = input("> ")

    if int(choice) == num1 - num2:
        print("Correct! Nice job! Keep on playing!\n")
        start_game()
    else:
        print(f"Incorrect...the answer is {num1-num2} !\n")
        start_game()

def multiplication():
    num1 = randint(0, 100)
    num2 = randint(0, 100)

    print(f"What is {num1} * {num2} ?\n")

    choice = input("> ")

    if int(choice) == num1 * num2:
        print("Correct! Nice job! Keep on playing!\n")
        start_game()
    else:
        print(f"Incorrect...the answer is {num1*num2} !\n")
        start_game()


start_game()
