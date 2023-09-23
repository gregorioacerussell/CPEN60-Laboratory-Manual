# 4. a.) Write a program that asks the user to enter a sentence and then randomly
# rearranges the words of the sentence. Don't worry about getting punctuation or
# capitalization correct.
from random import shuffle

sentence = input("Input a sentence: ").split(' ')
shuffle(sentence)
print(' '.join(sentence))