# 4. Write a program that asks the user to enter a password. If the user enters the right
# password, the program should tell them they are logged in to the system. Otherwise, the
# program should ask them to reenter the password. The user should get five tries to enter
# the password, after which point the program should tell them that they are kicked off of
# the system.

password = 'ace'
ask_password = input("Enter the password: ")

i = 5
while i > 1:
    if ask_password == password:
        print("You are now logged in!")
        break
    else:
        print(f"Wrong! You only {i-1} have tries left. ")
        i -= 1
        ask_password = input("Enter the password: ")
        continue
if i == 1:
    print("You have been kicked off the system.")
