# 2. Write a program that generates a list of 20 random numbers between
# 1 and 100.

# a.) Print the list.
import random
random_list = [random.randint(1,100) for i in range(20)]

print(random_list)