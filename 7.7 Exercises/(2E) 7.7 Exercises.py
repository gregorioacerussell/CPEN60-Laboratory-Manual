# 2. Write a program that generates a list of 20 random numbers between
# 1 and 100.

# e.) Print how many even numbers are in the list.

import random

random_list = [random.randint(1,100) for i in range(20)]
random_list_even = [i for i in random_list if i % 2 == 0]
print(f"There are {len(random_list_even)} even numbers in the list: \n{random_list}")