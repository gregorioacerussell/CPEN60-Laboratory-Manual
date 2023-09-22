# 3. (a) Ask the user to enter a sentence and print out the third word of the sentence.

sentence = input("Enter a sentence: ").split(' ')

for i in sentence:
    if i == sentence[2]:
        print(i)
