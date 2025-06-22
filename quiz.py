# SIMPLE QUIZ GAME IN PYTHON

qns = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "Most common gas in Earth's atmosphere?: ",
    "How many bones are there in the human body?: ",
    "Closest planet to the Sun?: "
)

opts = (
    ("A. 116", "B. 108", "C. 118", "D. 100"),
    ("A. Whale", "B. Shark", "C. Ostrich", "D. Hen"),
    ("A. Nitrogen", "B. Oxygen", "C. Carbon dioxide", "D. Ozone"),
    ("A. 206", "B. 103", "C. 200", "D. 20"),
    ("A. Earth", "B. Venus", "C. Uranus", "D. Mercury")
)

ans = ("C", "C", "A", "A", "D")

guesses = []
score = 0
question_num = 0

for qn in qns:
    print("\n---------------------------")
    print(qn)

    for opt in opts[question_num]:
        print(opt)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == ans[question_num]:
        score += 1
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        print(f"Correct answer: {ans[question_num]}")

    question_num += 1

# Final Score
print("\n===========================")
print(f"Your Score: {score}/{len(qns)}")
print("===========================")
