# 13. Write a program that asks the user to enter two strings of the same length.
# The program should then check to see if the strings are of the same length. If they
# are not, the program should print an appropriate message and exit. If they are of the
# same length, the program should alternate the characters of the two strings. For
# example, if the user enters abcde and ABCDE the program should print out AaBbCcDdEe.


word1 = input("Enter a word: ")
word2 = input("Enter a different word: ")
if len(word1) != len(word2):
    print("Error! The words doesn't have the same length.")
else:
    for i in range(len(word1)):
        print(word1[i], end='')
        print(word2[i], end='')
