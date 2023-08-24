# 12. Write a program that asks the user to guess a random number between 1 and 10.
# If they guess right, they get 10 points to added to their score, and they lose 1
# point for an incorrect guess. Give the user five numbers to guess and print their
# score after all the guessing is done.

import random

user_score = 0

for i in range(5):
    random_num = random.randint(1,10)
    while True:
        try:
            num = int(input(f"Try {i+1}: Guess the number between 1 and 10: "))
            if 1 < num > 10:
                print("Only input between 1 and 10.")
            else:
                break
        except ValueError:
            print("Invalid argument")
    if num == random_num:
        user_score += 10
        print("Correct!")
    else:
        user_score -= 1
        print("Wrong!")
if user_score < 0:
    user_score = 0
print(f"You got a score of {user_score}/50")