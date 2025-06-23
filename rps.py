import random

options = ("rock", "paper", "scissors")
player = None


while player not in options:
    player = input("Enter a choice (rock, paper, scissors): ")


computer = random.choice(options)

print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
    print("Its a tie! ")

elif player=="rock" and computer==" scisssors ":
    print("You won!")

elif player=="paper" and computer==" rock ":
    print("You Won!")

elif player=="scissor" and computer==" paper ":
    print("You Won!")

else:
    print("Computer Won")





