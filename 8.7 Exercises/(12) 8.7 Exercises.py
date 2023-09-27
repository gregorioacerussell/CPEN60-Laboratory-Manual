# 12. Write a program that gets a string from the user containing a potential telephone number.
# The program should print Valid if it decides the phone number is a real phone number, and
# Invalid otherwise. A phone number is considered valid as long as it is written in the form
# abc-def-hijk or 1-abc-def-hijk. The dashes must be included, the phone number should contain
# only numbers and dashes, and the number of digits in each group must be correct. Test your
# program with the output shown below.

sample_number = input("Enter a telephone number: ").split('-')
confirmation = False
if sample_number[0] == '1':
    if len(sample_number[1]) == 3:
        if len(sample_number[2]) == 3:
            if len(sample_number[3]) == 4:
                confirmation = True
elif len(sample_number[0]) == 3:
    if len(sample_number[1]) == 3:
        if len(sample_number[2]) == 4:
            confirmation = True
if confirmation:
    confirmation = "Valid"
else:
    confirmation = "Invalid"
print(confirmation)