# 13. In the last chapter there was an exercise that asked you to create a
# multiplication game for kids. Improve your program from that exercise to keep
# track of the number of right and wrong answers. At the end of the program, print
# a message that varies depending on how many questions the player got right.

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