# A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly
# how much candy is in the bowl, then you win all the candy. You ask the person in charge the
# following: If the candy is divided evenly among 5 people, how many pieces would be left
# over? The answer is 2 pieces. You then ask about dividing the candy evenly among 6 people,
# and the amount left over is 3 pieces. Finally, you ask about dividing the candy evenly among
# 7 people, and the amount left over is 2 pieces. By looking at the bowl, you can tell that there
# are less than 200 pieces. Write a program to determine how many pieces are in the bowl.

def find_candy_amount():
    for candies in range(1, 200):
        if candies % 5 == 2 and candies % 6 == 3 and candies % 7 == 2:
            return candies

candy_amount = find_candy_amount()
print(f"The candy jar contains approximately {candy_amount} pieces!")
