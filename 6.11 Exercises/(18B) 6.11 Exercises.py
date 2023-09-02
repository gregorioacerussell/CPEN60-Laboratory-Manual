# 18. The goal of this exercise is to see if you can mimic the behavior of the in operator and the
# count and index methods using only variables, for loops, and if statements.

# b.) Without using the count method, write a program that asks the user for a string and
# a letter and counts how many occurrences there are of the letter in the string.

word = input("Enter a word: ")
letter = input("Enter a letter: ")

letter_count = 0
for i in word:
    if i == letter:
        letter_count += 1
print(f"{letter} appeared {letter_count} times in {word}.")
