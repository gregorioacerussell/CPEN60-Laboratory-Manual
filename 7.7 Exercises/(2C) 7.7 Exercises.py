# 2. Write a program that generates a list of 20 random numbers between
# 1 and 100.

# c.) Print the largest and smallest values in the list.

import random
random_list = [random.randint(1,100) for i in range(20)]

print(f"The largest value in the list {random_list}\nis: {sorted(random_list)[len(random_list)-1]} while the smallest value in the list is: {sorted(random_list)[0]}")
