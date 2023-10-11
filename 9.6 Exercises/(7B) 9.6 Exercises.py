# 7. Recall that, given a string s, s.index('x') returns the index of the first x
# in s and an error if there is no x.

# (b) Write the above program using for/break loop instead of a while loop.

s = input("Enter a string: ")
s_letter = input("Enter a letter: ")
checker = False
for i in range(len(s)):
    if s[i] == s_letter:
        print(f"The letter {s_letter} is in index {s.index(s_letter)}.")
        checker = True
        break
if checker == False:
    print(f"The letter {s_letter} was not found in the inputted string.")