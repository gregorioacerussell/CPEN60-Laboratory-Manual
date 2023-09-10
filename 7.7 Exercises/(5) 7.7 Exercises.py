# 5. Ask the user to enter a list of strings. Create a new list that
# consists of those strings with their first characters removed.

list_string = input("Enter a list of strings (ex: red, blue, yellow): ").split(', ')

for string in list_string:
    print(string.replace(string[0], ''), end=' ')
