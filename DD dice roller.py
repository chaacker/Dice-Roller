import random

z = int(input("How many dice do you have? "))
if z > 1:
    x = []
    for i in range(z):
        a = int(input("What is the max of this dice? "))
        x.append(a)
elif z == 1:
    x = int(input("What's the max on your dice? "))
y = 1


answer = 'y'
if z == 1:
    while answer == "y" or answer == "Y":
        roll = random.randint(y, x)
        print("You rolled a", roll, "!")
        if roll == 20:
                print("Critical hit!")
        elif roll == 1:
            print("Big yikes, a blunder!")
        answer = input("Do you want to roll again? y or n: ")
elif z > 1:
    while answer == "y":
        die = []
        for i in x:
            roll = random.randint(y, i)
            die.append(roll)
        print("The numbers are: ", die)
        answer = input("Do you want to roll again? y or n: ")
