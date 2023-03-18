import random

num=random.randint(1,20)

while True:

    guess=int(input("Guess a Number between 1 to 20: "))

    if guess==num:
        print("You choose correct number")
        break

    elif guess>num:
        print("You choose a greater number")

    elif guess<num:
        print("You choose smaller number")
