# 14. This exercise is about the well-known Monty Hall problem. In the problem,
# you are a contestant on a game show. The host, Monty Hall, shows you tree
# doors. Behind one of those doors is a prize, and behind the other two doors are goats.
# You pick a door. Monty Hall, who knows behind which door the prize lies, then opens
# up one of the doors that doesn't contain the prize. There are now two doors left, and
# Monty gives you the opportunity to change your choice. Should you keep the same door,
# change doors, or does it not matter?

# a.) Write a program that stimulates playing this game 10000 times and calculate what
# percentage of the time you would win if you switch and what percentage of the time
# you would win by not switching?

import random
swap_score = 0
did_not_swap_score = 0
for i in range(10000):
    door = random.randint(1,3)
    choice = random.randint(1,3)
    if choice == door:
        second_choice = random.randint(1,2)
        if second_choice == 2:
            did_not_swap_score += 1
    else:
        second_choice = random.randint(1,2)
        if second_choice == 1:
            swap_score += 1
swap_score_percentage = (swap_score / 10000) * 100
did_not_swap_score_percentage = (did_not_swap_score / 10000) * 100

print(f"The win percentage for playing the game 10,000 times if you swapped doors is: {round(swap_score_percentage,2)} %")
print(f"The win percentage for playing the game 10,000 times if you did not swapped doors is: {round(did_not_swap_score_percentage,2)} %")