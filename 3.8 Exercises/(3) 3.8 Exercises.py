# 3. Write a program that generates a random number between 1 and 10 and prints
# your name that many times.

import random

random_number = random.randint(1,10)
print(f"The random number is {random_number}")
for i in range(random_number):
    print("Ace")