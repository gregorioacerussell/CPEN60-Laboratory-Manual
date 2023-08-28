# 4. Write a program that asks the user to enter a word and prints out whether that
# word contains any vowels.

vowels = ['a','e','i','o','u']

word = input("Enter anything: ")
vowel_checker = False

for i in word:
    for j in vowels:
        if i == j:
            vowel_checker = True

if vowel_checker:
    print(f"The word {word} contains vowels.")
else:
    print(f"The word {word} doesn't contains vowels.")



