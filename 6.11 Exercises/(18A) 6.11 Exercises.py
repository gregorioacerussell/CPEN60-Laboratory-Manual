# 18. The goal of this exercise is to see if you can mimic the behavior of the in
# operator and the count and index methods using only variables, for loops, and
# if statements.

# a.) Without using the in operator, write a program that asks the user for a string and
# a letter and prints out whether the letter appears in the string.

word = input("Enter a string: ")
letter = input("Enter a letter: ")

not_in_word = False
for i in word:
    if i == letter:
        print(f"{i} is in {word}.")
        not_in_word = False
        break
    else:
        not_in_word = True

if not_in_word:
    print(f"{letter} is not in {word}.")
