# 13. Write a program that removes any repeated items from a list so that each item
# appears at most once. For instance, the list [1, 1, 2, 3, 4, 0, 0] would become
# [1, 2, 3, 4, 0]

sample_list = input("Make a list (ex: 1, 2, 3, 4): ").split(', ')

print(sorted(set(sample_list)))

