# 15. When I was a kid, we used to play this game called Mad Libs. The way it worked
#  was a friend would ask me for some words and then insert those words into a story
# at specific places and read the story. The story would often turn out to be pretty funny
# with the words I had given since I had no idea what the story was about. The words were
# usually from a specific category, like a place, an animal, etc.

# For this problem you will write a Mad Libs program. First, you should make up a story
# and leave out some words of the story. Your program should ask the user to enter some
# words and tell them what types of words to enter. Then print the full story along with
# the inserted words.

print("Welcome to my Mad Libs! Please input the words asked :)")
adjective1 = input("Enter an adjective: ")
nationality = input("Enter a nationality: ")
person = input("Enter a person: ")
noun1 = input("Enter a noun: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
adjective3 = input("Enter another adjective: ")
adjective4 = input("Enter another adjective: ")
plural_noun = input("Enter a plural noun: ")
noun3 = input("Enter another noun: ")
number1 = input("Enter a number: ")
shapes = input("Enter a shape (plural): ")
food = input("Enter a food: ")
food2 = input("Enter another food: ")
number2 = input("Enter another number: ")

print(f"Pizza was invented by a {adjective1} {nationality} chef named {person}. "
      f"To make a pizza, you need to take a lump of {noun1}, and make a thin, "
      f"round {adjective2} {noun2}. Then you cover it with {adjective3} sauce, "
      f"{adjective4} cheese, and fresh chopped {plural_noun}. Next you have to bake it "
      f"in a very hot {noun3}. When it is done, cut it into {number1} {shapes}. Some kids"
      f" like {food2} pizza. If I could, I would eat pizza {number2} times a day!")