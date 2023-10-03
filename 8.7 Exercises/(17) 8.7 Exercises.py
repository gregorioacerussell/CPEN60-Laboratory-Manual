# 17. Write a program that finds the average of all the
# entries in a 4 x 4 list of integers.

sample_list = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]
sums = []
total = []
for i in range(len(sample_list)):
    sums.append(sum(sample_list[i]))
for j in range(len(sample_list)):
    total.append(len(sample_list[j]))
print(f"The average of all the entries in a 4x4 list of integers"
      f" is: {sum(sums) / sum(total)}")
