# 6. Create the following lists using a for loop.
# c.) The list ['a', 'bb', 'ccc', 'dddd', ...] that ends with 26 copies of
# the letter z.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
sample_list = []


for i in range(len(alphabet)):
        sample_list.append(alphabet[i]*int(i+1))
print(sample_list)