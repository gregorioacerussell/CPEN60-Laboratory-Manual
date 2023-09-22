# 3. (b) Ask the user to enter a sentence and print out every third word of the sentence.

sentence = input("Input a sentence: ").split(' ')

for word in range(1, len(sentence)+1):
    if word % 3 == 0:
        print(sentence[word-1])

