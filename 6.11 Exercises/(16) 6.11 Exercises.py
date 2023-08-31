# 16. Companies often try to personalize their offers to make them more attractive.
# One simple way to do this is just to insert the person's name at various places in the
# offer. Of course, companies don't manually type in every person's name; everything is
# computer-generated. Write a program that asks the user for their name and then generates
# an offer. For simplicity's sake, you may assume that the person's first and last names
# are one word each.

name = input("Enter name: ")
short_name = []
for i in name:
    if i == ' ':
        break
    else:
        short_name.append(i)
print()
print(f"Dear {name},")
print()
print(f"I am pleased to offer you our new Platinum Plus Rewards card at a special "
      f"introductory APR of 47.99%. {''.join(map(str,short_name))}, an offer like this does not come along "
      f"every day, so I urge you to call now toll-free at 1-800-314-1592. We cannot "
      f"offer such a low rate for long, {''.join(map(str,short_name))}, so call right away.")