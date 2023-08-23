# 10. Ask the user to enter 10 test scores. Write a program to do the following:
# d.) If any of the scores is greater than 100, then after all the scores have been
# entered, print a message warning the user that a value over 100 has been entered.

while True:
    try:
        test_scores = list(map(int, input("Enter 10 test scores: ").split()))
        if len(test_scores) == 10:
            break
        else:
            print("Please input 10 test scores!")
    except ValueError:
        print("Invalid argument")
warning = False
for i in range(1, len(test_scores)):
    if test_scores[i] > 100:
        warning = True
        break

if warning:
    print("Warning! There is a score greater than 100 inputted.")
