# A more general version of the above technique is the rail fence cipher,
# where instead of breaking things into evens and odds, they are broken up
# by threes, fours or something larger. For instance, in the case of threes,
# the string secret message would be broken into three groups. The
# first group is sr sg, the characters at indices 0, 3, 6, 9 and 12.
# The second group is eemse, the characters at indices 1, 4, 7, 10, and 13.
# The last group is ctea, the characters at indices 2, 5, 8,
# and 11. The encrypted message is sr sgeemsectea.

word = input("Enter a word to encrypt: ")
group1_index = [i for i in range(len(word)) if i == 0 or i % 3 == 0]
group2_index = [i+1 for i in range(len(word)) if i == 0 or i % 3 == 0]
group3_index = [i+2 for i in range(len(word)) if i == 0 or i % 3 == 0 and i + 2 < len(word)]

group1 = [word[i] for i in group1_index]
group2 = [word[i] for i in group2_index]
group3 = [word[i] for i in group3_index]

print(f"The encrypted is message: {''.join(map(str, (group1 + group2 + group3)))}")


