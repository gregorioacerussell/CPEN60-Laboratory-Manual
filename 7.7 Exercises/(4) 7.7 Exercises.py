# 4. Ask the user to enter a list containing numbers between 1 and 12.
# Then replace all of the entries in the list that are greater than 10
# with 10.

sample_list = input("Enter a list containing numbers between 1 and 12 \n(ex: 1, 3, 12, 11, 9): ").split(', ')

for num in range(len(sample_list)):
    if int(sample_list[num]) > 10:
        sample_list[num] = 10
print(sample_list)

