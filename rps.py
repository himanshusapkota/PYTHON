import random

def rps():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user = input("Choose rock, paper or scissors: ").lower()
        if user not in choices:
            print("Invalid choice.")
            continue
        comp = random.choice(choices)
        print(f"Computer chose {comp}.")
        if user == comp:
            print("It's a tie!")
        elif (user == 'rock' and comp == 'scissors') or (user == 'scissors' and comp == 'paper') or (user == 'paper' and comp == 'rock'):
            print("You win!")
        else:
            print("You lose.")
        again = input("Play again? (yes/no): ").lower()
        if again != 'yes':
            break

rps()
