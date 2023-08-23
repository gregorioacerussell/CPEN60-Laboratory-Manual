# 10. Ask the user to enter 10 test scores. Write a program to do the following:
# c.) Print out the second largest score.

while True:
    try:
        test_scores = list(map(int, input("Enter 10 test scores: ").split()))
        if len(test_scores) == 10:
            break
        else:
            print("Please enter 10 test scores!")
    except ValueError:
        print("Invalid argument")

test_scores.sort()
print(f"The second largest score is {test_scores[-2]}.")