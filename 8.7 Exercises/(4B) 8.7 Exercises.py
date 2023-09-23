# 4. b.) Do the above problem, but now make sure that the sentence starts with a
# capital, that the original first word is not capitalized if it comes in the middle
# of the sentence, and that the period is in the right place.

from random import shuffle

sentence = input("Input a sentence: ").split(' ')
if sentence[-1].endswith('.'):
    sentence[-1] = sentence[-1][:-1]
shuffle(sentence)
new_sentence = ' '.join(sentence)
new_sentence = new_sentence.capitalize()  # Capitalize the sentence
print(new_sentence + '.')
