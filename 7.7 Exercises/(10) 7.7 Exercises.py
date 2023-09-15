# 10. Write a program that rotates the elements of a list so that the element at the
# first index moves to the second index, the element in the second index moves to the
# third index, etc., and the element in the last index moves to the first index.

# should print out: [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sample_list = [1,2,3,4,5,6,7,8,9,10]
print([sample_list[-1]] + sample_list[0:-1])