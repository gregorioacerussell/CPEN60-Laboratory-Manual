# 18. Write a program that creates a 10x10 list of random integers between
# 1 and 100. Then do the following:

# a. Print the list.
from random import randint

sample_list = [[randint(1,100) for i in range(10)] for j in range(10)]
print(sample_list)
