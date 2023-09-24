# 6. Write a simple lottery drawing program. The lottery drawing should consist of
# six different numbers between 1 and 48.

from random import randint

lottery_numbers = []
for i in range(6):
    lottery_numbers.append(randint(1, 48))
print(f"The random numbers generated is: {'-'.join(map(str,lottery_numbers))}")