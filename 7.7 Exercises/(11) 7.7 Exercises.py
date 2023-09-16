# 11. Using a for loop, create the list below, which consists of ones separated by
# increasingly many zeroes. The last two ones in the list should be separated by ten
# zeroes.

# [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, ...]

sample_list = [1]
for i in range(1,11):
    sample_list.append(1)
    for j in range(i):
        sample_list.append(0)
print(sample_list)