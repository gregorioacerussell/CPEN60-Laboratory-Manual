# 11. Write a program that asks the user to enter a word that contains the letter a.
# The program should then print the following two lines: On the first line should be
# the part of the string up to and including the first a, and on the second line should
# be the rest of the string. Sample output is shown below:
# Enter a word: buffalo
# buffa
# lo

while True:
    word = input("Enter a word: ")
    if word.isalpha():
        break
    else:
        print("Please enter a word.")

for i in range(len(word)):
    if word[i] == 'a':
        for j in range(i+1):
            print(word[j], end='')
        print()
        for z in range(i+1, len(word)):
            print(word[z], end='')

