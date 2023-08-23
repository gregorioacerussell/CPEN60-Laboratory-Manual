# 10. Ask the user to enter 10 test scores. Write a program to do the following.
# e.) Drop the two lowest scores and print out the average of the rest of them.

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
test_scores.pop(0)
test_scores.pop(0)
average = sum(test_scores) / len(test_scores)
print(test_scores)
print(f"The average of the 8 test scores is {average}.")