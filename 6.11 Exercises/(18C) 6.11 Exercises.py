# 18. The goal of this exercise is to see if you can mimic the behavior of the in operator and the
# count and index methods using only variables, for loops, and if statements.

# c.) Without using the index method, write a program that asks the user for a string
# and a letter and prints out the index of the first occurrence of the letter in the string.
# if the letter is not in the string, the program should say so.

word = input("Enter a word: ")
letter = input("Enter a letter: ")

not_in_string = False
for i in range(len(word)):
    if letter == word[i]:
        print(f"The first occurrence of the letter {letter} was in index {i}.")
        not_in_string = False
        break
    else:
        not_in_string = True

if not_in_string:
    print(f"{letter} was not found in the string {word}.")