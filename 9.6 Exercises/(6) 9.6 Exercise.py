# 6. Modify the higher/lower program so that when there is only one guess left, it says
# 1 guess, not 1 guesses.

from random import randint
rand_num = randint(1,10)
attempts = 5

while attempts > 0:
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == rand_num:
        print("You won!")
        break
    else:
        attempts -= 1
        if attempts == 1:
            print("Wrong! You have one guess left.")
        elif attempts == 0:
            print(f"You ran out of attempts. The correct number is {rand_num}")
        else:
            print(f"Wrong! You have {attempts} guesses left.")