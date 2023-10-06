# 2. (b) Modify the program above to print out every second character
# of the string.

sample_sentence = input("Enter a sentence: ")

i = 1
while i < len(sample_sentence):
    print(sample_sentence[i])
    i += 2