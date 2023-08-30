# 12. Write a program that asks the user to enter a word and then capitalizes every
# other letter of that word. So if user enters rhinoceros, the program should print
# rHiNoCeRoS.

word = input("Enter a word: ")

for i in range(len(word)):
    if i % 2 == 0:
        print(word[i],end='')
    else:
        print(word[i].upper(),end='')


