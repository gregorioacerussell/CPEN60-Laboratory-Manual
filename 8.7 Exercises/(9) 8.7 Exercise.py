# 9. Write a simple quiz game that has a list of ten questions and a list of
# answers to those questions. The game should give the player four randomly
# selected questions to answer. It should ask the questions one-by-one, and tell the
# player whether they got the question right or wrong. At the end it should print out
# how many out of for they got right.

questions = [
    "What's 9+10?: ",
    "What is Victoria's Secret?: ",
    "What again is 9+10?: "
]

answers = [
    "21",
    "secret",
    "19"
]

score = 0
print("Welcome to My Super Simple Quiz!")
for i in range(len(questions)):
    user = input(questions[i]).lower()
    if user == answers[i]:
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The answer is {answers[i]}")
print(f"Congrats you got {score} correct! ")