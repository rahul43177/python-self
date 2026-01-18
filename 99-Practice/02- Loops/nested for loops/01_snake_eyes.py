"""
Instructions
Suppose we have a pair of dice. 🎲 🎲
In dice games, "snake eyes" means rolling two 1s. Why is it called that? Because two small dots look like a pair of snake eyes. 🐍👀
It’s the lowest possible roll (1 + 1 = 2) and is seen as bad luck. 😅
Let's keep rerolling two dice until we get snake eyes.

Nope
Nope
Nope
Nope
Snake eyes!

First, use the random module to “roll” the two dice.
Each die (named die1 and die2) should have an integer value from 1 to 6.
Store the sum of the two random values in variable named total.
Using a while loop, check if total is 2. If it isn't, print the string 'Nope' and keep "rerolling" the dice.
Let the loop run until the total is 2, then print 'Snake eyes!
"""

from random import randint 

die1 = randint(1,6) 
die2 = randint(1,6) 

while(die1 + die2 != 2) :
    print("Nope")
    die1 = randint(1,6)
    die2 = randint(1,6)

print("Snake eyes!")