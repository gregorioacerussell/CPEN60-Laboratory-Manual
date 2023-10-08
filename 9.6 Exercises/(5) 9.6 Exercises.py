# 5. Write a program that allows the user to enter any number of test scores.
# The user indicates they are done by entering in a negative number. Print how many
# of the scores are A's (90 or above). Also print out the average.

i = True
scores = []
score_90 = 0
while i:
    test_score = int(input("Enter a test score (input a negative number to stop the cycle): "))
    if test_score < 0:
        break
    else:
        scores.append(test_score)
    for j in scores:
        if j >= 90:
            score_90 += 1
print(f"There are {score_90} A's in the scores inputted.\nThe average score in the test scores inputted is {sum(scores) / len(scores)}")
