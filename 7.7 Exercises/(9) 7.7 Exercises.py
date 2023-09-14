# When playing games where you have to roll two dice, it is nice to know the odds of
# each roll. For instance, the odds of rolling a 12 are about 3%, and the odds of
# rolling a 7 are about 17%. You can compute these mathematically, but if you don't know
# the math, you can write a program to do it. To do this, your program should simulate
# rolling two dice about 10,000 times and compute and print out the percentage of rolls
# that come out to be 2, 3, 4, ..., 12.

import random

d1 = [1,2,3,4,5,6]
d2 = [1,2,3,4,5,6]

sum_dice2 = 0
sum_dice3 = 0
sum_dice4 = 0
sum_dice5 = 0
sum_dice6 = 0
sum_dice7 = 0
sum_dice8 = 0
sum_dice9 = 0
sum_dice10 = 0
sum_dice11 = 0
sum_dice12 = 0

for i in range(1, 10001):
    d1_choice = random.randint(0,5)
    d2_choice = random.randint(0,5)
    probability = d1[d1_choice] + d2[d2_choice]
    if probability == 2:
        sum_dice2 += 1
    elif probability == 3:
        sum_dice3 += 1
    elif probability == 4:
        sum_dice4 += 1
    elif probability == 5:
        sum_dice5 += 1
    elif probability == 6:
        sum_dice6 += 1
    elif probability == 7:
        sum_dice7 += 1
    elif probability == 8:
        sum_dice8 += 1
    elif probability == 9:
        sum_dice9 += 1
    elif probability == 10:
        sum_dice10 += 1
    elif probability == 11:
        sum_dice11 += 1
    elif probability == 12:
        sum_dice12 += 1

ask_user = int(input("Choose the value from (2-12): "))
if ask_user == 2:
    print(f"The probability of rolling the value 2 from 2 dices about 10,000 times are {round((sum_dice2/10000)*100, 2)}%")
if ask_user == 3:
    print(f"The probability of rolling the value 3 from 2 dices about 10,000 times are {round((sum_dice3/10000)*100, 2)}%")
if ask_user == 4:
    print(f"The probability of rolling the value 4 from 2 dices about 10,000 times are {round((sum_dice4/10000)*100, 2)}%")
if ask_user == 5:
    print(f"The probability of rolling the value 5 from 2 dices about 10,000 times are {round((sum_dice5/10000)*100, 2)}%")
if ask_user == 6:
    print(f"The probability of rolling the value 6 from 2 dices about 10,000 times are {round((sum_dice6/10000)*100, 2)}%")
if ask_user == 7:
    print(f"The probability of rolling the value 7 from 2 dices about 10,000 times are {round((sum_dice7/10000)*100, 2)}%")
if ask_user == 8:
    print(f"The probability of rolling the value 8 from 2 dices about 10,000 times are {round((sum_dice8/10000)*100, 2)}%")
if ask_user == 9:
    print(f"The probability of rolling the value 9 from 2 dices about 10,000 times are {round((sum_dice9/10000)*100, 2)}%")
if ask_user == 10:
    print(f"The probability of rolling the value 10 from 2 dices about 10,000 times are {round((sum_dice10/10000)*100, 2)}%")
if ask_user == 11:
    print(f"The probability of rolling the value 11 from 2 dices about 10,000 times are {round((sum_dice11/10000)*100, 2)}%")
if ask_user == 12:
    print(f"The probability of rolling the value 12 from 2 dices about 10,000 times are {round((sum_dice12/10000)*100, 2)}%")
