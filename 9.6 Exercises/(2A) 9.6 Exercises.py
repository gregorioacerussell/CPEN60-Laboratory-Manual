# 2. (a) Write a program that uses a while loop (not a for loop) to read
# through a string and print the characters of the string one-by-one on
# separate lines.

sample_string = input("Enter a sentence: ")

i = 0
while i < len(sample_string):
    print(sample_string[i])
    i += 1


