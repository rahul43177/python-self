"""
Instructions

Ever wonder how many people live in New York City? What about London?

Create a favorite_cities.py program.

Let's make a City class that uses the __init__() method to define the following attributes:

    name (string)
    country (string)
    population (integer rounded to the nearest thousand people)
    landmarks (list of strings)

Next, create an object for your hometown and assign the attributes above.

Lastly, create another object for the city that you've always wanted to visit!

Bonus: Add 2-3 more attributes, like nickname, founding year, mayor, etc.
"""

class City:
    def __init__(self , name , country , population , landmarks , nickname = "No Nickname" , founding_year ="unknown" , mayor ="Unknown"):
        self.name = name ,
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.nickname = nickname
        self.founding_year = founding_year
        self.mayor = mayor


bhind = City("Bhind" , "India" , 500000 , "Gwalior")

kashmir = City("Kashmir" , "India" , 1000000 , "Near SriNagar" , "Jannat" , 1995, "huhuhuu" )

print(vars(bhind))
print(vars(kashmir))