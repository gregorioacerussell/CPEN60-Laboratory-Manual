# 1.  Write a program that asks the user to enter a string. The program should then print the
# following:

# g.) The seventh character of the string if the string is long enough and a message
# otherwise

while True:
    string = input("Enter anything: ")
    if len(string) <= 7:
        print("Enter a string with seven or more characters.")
    else:
        print(f"The seventh character in {string} is: {string[6]}")
        break
        
