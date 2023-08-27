# 2. A simple way to estimate the number of words in a string is to count the numbers
# of spaces in the string. Write a program that asks the user for a string and returns
# an estimate of how many words are in the string.

words = input("Enter anything: ")
word = 1
for i in words:
    if i == ' ':
        word += 1

print(f"There is an estimated of {word} words inputted in: {words}")


