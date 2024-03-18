import random

sides = int(input("How many dice do you have? "))
if sides > 1:
    x = []
    for i in range(sides):
        a = int(input("What is the max of this dice? "))
        x.append(a)
elif sides == 1:
    x = int(input("What's the max on your dice? "))

answer = "y"
if sides == 1:
    while answer == "y" or answer == "Y":
        roll = random.randint(1, x)
        print(f"You rolled a {roll}!")
        if roll == 20:
                print("Critical hit!")
        elif roll == 1:
            print("Big yikes, a blunder!")
        answer = input("Do you want to roll again? y or n: ")
elif sides > 1:
    while answer == "y" or answer == "Y":
        die = []
        for i in x:
            roll = random.randint(1, i)
            die.append(roll)
        print("The numbers are: ", die)
        answer = input("Do you want to roll again? y or n: ")
