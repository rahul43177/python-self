"""
# Random Choices
Let's revisit a module we've already worked with before: the random module!
Remember when we used the .randint() method to generate a random number in the Magic 8 Ball? Well, there are 22 methods total in the random module.
Here's another method, .choices(), in action:
import random
dice = [1, 2, 3, 4, 5, 6]
print(random.choices(dice))
    The import keyword is used to access the random module.
    The .choices() method will randomly select a single item by default.
We can also set how many items are randomly chosen with the k parameter:
import random
dice = [1, 2, 3, 4, 5, 6]
print(random.choices(dice, k=3))
This will return a new list of three items randomly selected from dice. Every time you run it, the output should be different.
Note: The k parameter only sets the length of the returned list from .choices(). This means that a list item may be included in the returned list more than once.
"""
import random
from random import choices
dice = [1,2,3,4,5,6]

print(random.choices(dice)) #It will take a random value from the array itself

#we can ask for more random values instead of single value

three_vals = random.choices(dice , k = 3)

for i in range(1, len(three_vals)):
    print(f" index : {i} and value : {three_vals[i]}")
    if three_vals[i] == three_vals[i-1] :
        print("same")
    else :
        print("diff")