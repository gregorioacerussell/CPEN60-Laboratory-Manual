# 5. Generate a random number between 1 and 10. Ask the user to guess the number and
# print a message based on whether they get it right or not.

import random

random_number = random.randint(1,10)

while True:
    try:
        user_number = int(input("Enter a random number between 1 and 10: "))
        if user_number == random_number:
            print("You guessed correctly!")
            break
        elif user_number > 10:
            print("Invalid input.")
            continue
        else:
            print("You made a wrong guess.")
            break
    except ValueError:
        print("Invalid argument")