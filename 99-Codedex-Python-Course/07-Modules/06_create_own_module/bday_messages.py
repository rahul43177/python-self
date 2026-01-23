"""
## bday_messages.py

Create a new file called bday_messages.py.

Import the random module.

Then, define a bday_messages list with the following items:

    'Hope you have a very Happy Birthday! 🎈',
    'It's your special day – get out there and celebrate! 🎉',
    'You were born and the world got better – everybody wins! 🥳',
    'Have lots of fun on your special day! 🎂',
    'Another year of you going around the sun! 🌞'

Next, use the random.choice() method to get a single item from the list.

Save this item in a random_message variable.

Let's save bday_messages.py and move to the next part.
"""
from random import choice

bday_messages = [
    'Hope you have a very Happy Birthday! 🎈',
    "It's your special day – get out there and celebrate! 🎉",
    'You were born and the world got better – everybody wins! 🥳',
    'Have lots of fun on your special day! 🎂',
    'Another year of you going around the sun! 🌞'
]

random_message = choice(bday_messages)
