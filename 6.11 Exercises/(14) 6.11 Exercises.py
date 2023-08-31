# 14. Write a program that asks the user to enter their name in lowercase and then
# capitalizes the first letter of each word of their name.

while True:
    name = input("Enter your name: ")
    if name != name.lower():
        print("Error! Name must be all in lowercase")
    else:
        print(name.title())
        break

