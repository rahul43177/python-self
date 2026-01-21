'''
Fortune Cookie is a small cookie wafer with a piece of paper inside, called a “fortune”, which is usually a Chinese phrase with translation and a list of lucky numbers. They are served in restaurants in the U.S. and Canada. 🥠

Create a fortune_cookie.py program that gives the user random fortunes.

Define a function named fortune(). Inside the function, print out a random fortune from the list of options below:

    Don't pursue happiness – create it.
    All things are difficult before they are easy.
    The early bird gets the worm, but the second mouse gets the cheese.
    Someone in your life needs a letter from you.
    Don't just think. Act!
    Your heart will skip a beat.
    The fortune you search for is in another cookie.
    Help! I'm being held prisoner in a Chinese bakery!

Make sure to use the random module's random.randint() and an if/elif/else.

Then, call the fortune() function three times and see what you get!

Bonus: If you're daring, rewrite the function without an if/elif/else.
'''


fortune_lists = [
    "Don't pursue happiness – create it.",  # 0 
    "All things are difficult before they are easy.",#1
    "The early bird gets the worm, but the second mouse gets the cheese.",#2
    "Someone in your life needs a letter from you.",#3
    "Don't just think. Act!",#4
    "Your heart will skip a beat.",#5
    "The fortune you search for is in another cookie.", #6 
    "Help! I'm being held prisoner in a Chinese bakery!" #7
]

print(len(fortune_lists))



import random
def fortune() : 
    size = len(fortune_lists)
    random_number = random.randint(0,size-1)
    print(fortune_lists[random_number])
    
fortune()