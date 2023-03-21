import random

l=["Rock","Paper","Scissor"]
computer=random.choice(l)

user=input("Choice(Rock,Paper,Scissor):")

if user==computer:
    print("Draw")
elif user=="Rock" and computer=="Paper":
    print("Computer wins")
elif user=="Paper" and computer=="Scissor":
    print("Computer wins")
elif user=="Scissor" and computer=="Rock":
    print("Computer wins")
elif user=="Paper" and computer=="Rock":
    print("user wins")
elif user=="Scissor" and computer=="Paper":
    print("User wins")
elif user=="Rock" and computer=="Scissor":
    print("User wins")

