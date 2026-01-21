"""
Instructions

Snapple is a famous tea drink brand from Queens, New York. 
Each bottle cap comes with a silly fun fact.

Use the random module to create a number from 0 to 5.

Then use an if/elif/else statement to print out one of these six random Snapple facts:

    0 - 'Flamingos turn pink from eating shrimp.'
    1 - 'The only food that doesn\'t spoil is honey.'
    2 - 'Shrimp can only swim backwards.'
    3 - 'A taste bud\'s life span is about 10 days.'
    4 - 'It is impossible to sneeze while sleeping.'
    5 - 'It is illegal to sing off-key in North Carolina.'
"""

from random import randint

random_number = randint(0,5)
print("Random number : " , random_number)
# facts = {
#      0 : 'Flamingos turn pink from eating shrimp.' , 
#     1 : 'The only food that doesn\'t spoil is honey.' , 
#     2 : 'Shrimp can only swim backwards.' , 
#     3 : 'A taste bud\'s life span is about 10 days.' , 
#     4 : 'It is impossible to sneeze while sleeping.' , 
#     5 : 'It is illegal to sing off-key in North Carolina.' 
# }
if random_number == 0 : 
    print("Flamingos turn pink from eating shrimp.")
elif random_number == 1 :
    print("The only food that doesn't spoil is honey.")
elif random_number == 2 :
    print("Shrimp can only swim backwards.")
elif random_number == 3 :
    print("A taste bud's life span is about 10 days.")
elif random_number == 4 :
    print("It is impossible to sneeze while sleeping.")
elif random_number == 5 :
    print("It is illegal to sing off-key in North Carolina.")

# print(facts[random_number])

#according to the questions 




