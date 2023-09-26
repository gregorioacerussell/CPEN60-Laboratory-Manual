# 10. Write a censoring program. Allow the user to enter some text and your program should print out the text 
# with all the curse words starred out. The number of stars should match the length of the curse word. For 
# the purposes of this program, just use the "curse" words darn, dang, freaking, heck, and shoot.

sample_sentence = input("Enter some text: ").split(' ')
curse_words = ['darn', 'dang', 'freaking', 'heck', 'shoot']
for i in range(len(sample_sentence)):
    if sample_sentence[i] in curse_words:
        sample_sentence[i] = '*'*len(sample_sentence[i])
print(' '.join(map(str,sample_sentence)))

    