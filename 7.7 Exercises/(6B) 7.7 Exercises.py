# 6. Create the following lists using a for loop.
# b.) A list containing the squares of the integers 1 through 50.

sample_list = []
for i in range(1,51):
    sample_list.append(i**2)
print(sample_list)