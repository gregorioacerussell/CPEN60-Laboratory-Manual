# 11. Section 8.3 described how to use the shuffle method to create a random anagram of a string.
# Use the choice method to create a random anagram of a string.

from random import choice

sample_word = input("Enter a word")
shuffled_word = []

for i in range(len(sample_word)):
    char = choice(sample_word)
    shuffled_word.append(char)
    sample_word = sample_word.replace(char, '', 1)
print(''.join(map(str, shuffled_word)))