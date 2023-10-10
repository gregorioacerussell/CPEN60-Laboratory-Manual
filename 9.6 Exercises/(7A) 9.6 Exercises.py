# 7. Recall that, given a string s, s.index('x') returns the index of the first x
# in s and an error if there is no x.

# (a) Write a program that asks the user for a string and a letter. Using a while loop,
# the program should print the index of the first occurrence of that letter and a
# message if the string does not contain the letter.

s_string = input("Enter a string: ")
s_letter = input("Enter a letter: ")

i = 0
while i < len(s_string):
    if s_letter == s_string[i]:
        print(f"The index of the first letter {s_letter} in {s_string} is in {s_string.index(s_letter)}.")
        break
    else:
        i += 1
if i == len(s_string):
    print(f"The string does not contain the letter {s_letter}.")