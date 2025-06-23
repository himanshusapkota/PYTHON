import random

# Generate a random number between 1 and 100
answer = random.randint(1, 100)

is_running = True
print("||----------------------------------------------||")
print("               NUMBER GUESSING GAME              ")
print("||----------------------------------------------||")
print("Enter a number between 1 and 100")

while is_running:
    gss = input("Enter your guess: ")

    if gss.isdigit():
        gs = int(gss)
        gs += 1

        if gs < 1 or gs > 100:
            print("Invalid! Out of range")
            print("Enter a number between 1 and 100")

        elif gs < answer:
            print("Too Low")

        elif gs > answer:
            print("Too High")

        else:
            print(f"Correct Number is {answer}")
            is_running = False
    else:

        print("Invalid Number")
        print("Enter a number between 1 and 100")
