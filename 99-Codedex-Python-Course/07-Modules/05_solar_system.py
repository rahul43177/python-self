from math import pi
from random import choices as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

"""If
random_planet is 'Mercury', then
r is 2440.
Else,
if random_planet is 'Venus', then r is 6052.
Else,
if random_planet is 'Earth', then r is 6371.
Else,
if random_planet is 'Mars', then r is 3390.
Else,
if random_planet is 'Saturn', then r is 58232.
Else, print
"Oops! An error occurred." to the console.
"""