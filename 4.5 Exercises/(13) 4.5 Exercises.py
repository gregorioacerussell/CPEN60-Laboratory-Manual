# 13. Wrote a program that lets the user play Rock-Paper-Scissors against the computer.
# There should be five rounds, and after those five rounds, your program should print
# out who won and lost or that there is a tie.

import random
user_score = 0
bot_score = 0
for i in range(1,6):
    bot = random.randint(1,3)
    user = int(input(f"Match {i}: Enter Rock (1), Paper (2), or Scissors (3): "))

    if user == 1 and bot == 1:
        bot_score += 1
        user_score += 1
        print("It was a tie")
    elif user == 1 and bot == 2:
        bot_score += 1
        print("Bot won")
    elif user == 1 and bot == 3:
        user_score += 1
        print("User won")
    elif user == 2 and bot == 1:
        user_score += 1
        print("User won")
    elif user == 2 and bot == 2:
        user_score += 1
        bot_score += 1
        print("It was a tie")
    elif user == 2 and bot == 3:
        bot_score += 1
        print("Bot won")
    elif user == 3 and bot == 1:
        bot_score += 1
        print("Bot won")
    elif user == 3 and bot == 2:
        user_score += 1
        print("User won")
    elif user == 3 and bot == 3:
        user_score += 1
        bot_score += 1
        print("It was a tie")
print()
if user_score > bot_score:
    print(f"You won with a score of {user_score} against {bot_score}")
elif user_score < bot_score:
    print(f"You lost with a score of {user_score} against {bot_score}")
elif user_score == bot_score:
    print(f"It was a tie between the bot, you both had a score of {user_score}")
