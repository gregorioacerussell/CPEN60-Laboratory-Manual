# 10. Write a multiplication game program for kids. The program should give the
# player ten randomly generated multiplication questions to do. After each, the
# program should tell them whether they got it right or wrong and what the correct
# answer is.

import random

score = 0
for i in range(1, 11):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = num1*num2
    while True:
        try:
            question = int(input(f"Question {i}: {num1} x {num2} = "))
            break
        except ValueError:
            print("Invalid argument")
    if question == answer:
        print("Right!")
        score += 1
    else:
        print("Wrong.")
print()
print(f"You got {score} out of 10")