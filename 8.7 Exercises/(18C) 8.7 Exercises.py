# 18. Write a program that creates a 10x10 list of random integers between
# 1 and 100. Then do the following:

# c. Find the smallest value in the sixth column
from random import randint

sample_list = [[randint(1,100) for i in range(10)] for j in range(10)]
sixth_column = [sample_list[k][5] for k in range(10)]
print(min(sixth_column))
