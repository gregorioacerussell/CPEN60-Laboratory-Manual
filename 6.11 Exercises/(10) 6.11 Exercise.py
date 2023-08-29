# 10. Write a program that asks the user to enter a string, then prints out each
# letter of the string doubled and on a separate line. For instance, if the user
# entered HEY, the output would be:
# HH
# EE
# YY

while True:
    word = input("Enter a word: ")
    if word.isalpha():
        break
    else:
        print("Please input a word.")

for i in word:
    print(i*2)