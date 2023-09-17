# 12. Write a program that generates 100 random integers that are either 0 or 1. Then
# find the longest run of zeros, the largest number of zeros in a row. For instance, the
# longest run of zeroes in [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0] is 4.

from random import randint

sample_list = []
maxzero = 0
list_count = 0
for i in range(100):
    sample_list.append(randint(0,1))
for i in range(len(sample_list)):
    if sample_list[i] == 0:
        list_count += 1
    if sample_list[i] == 1:
        if list_count > maxzero:
            maxzero = list_count
        list_count = 0
print(sample_list)
print(f"The largest number of zeros in a row are {maxzero}")


