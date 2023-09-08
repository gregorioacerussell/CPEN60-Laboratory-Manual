# 2. Write a program that generates a list of 20 random numbers between
# 1 and 100.

# b.) Print the average of the elements in the list.

import random

random_list = [random.randint(1,100) for i in range(20)]
print(f"The average of the random list {random_list} is: {sum(random_list)/len(random_list)}")