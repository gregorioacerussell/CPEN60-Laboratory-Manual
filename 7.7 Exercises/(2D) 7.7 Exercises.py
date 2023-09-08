# 2. Write a program that generates a list of 20 random numbers between
# 1 and 100.

# d.) Print the second largest and second smallest entries in the list.

import random
random_list = [random.randint(1,100) for i in range(20)]

print(f"The second largest value in list {random_list}\nis: {sorted(random_list)[len(random_list)-2]} while the second smallest value in the list is: {sorted(random_list)[1]}")