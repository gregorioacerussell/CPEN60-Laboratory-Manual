# 1. Write a program that asks the user to enter some text and then counts how many
# articles in the text. Articles are the words 'a', 'an', and 'the'.
import string

text = input("Enter some text/sentence: ").lower()
remove_punctuation = str.maketrans('', '', string.punctuation)
cleaned_text = text.translate(remove_punctuation).split(' ')
articles = 0
for word in cleaned_text:
    if word in ['a', 'an', 'the']:
        articles += 1
print(f"There are {articles} articles in the sentence inputted.")
