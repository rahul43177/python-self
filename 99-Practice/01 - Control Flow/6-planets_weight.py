"""
Instructions

The year is 2199... we have become an interplanetary species and can travel to other planets in the solar system! 🚀

Create a weight conversion program that:

    Asks the user what their Earth weight is (as a float).
    Asks the user for a planet number (as an int).

Then, use an if/elif/else statement to calculate the user's weight on the destination planet.

To calculate the user's weight:
destination weight=Earth weight × relative gravity
Number	Planet	Relative Gravity
1	Mercury	0.38
2	Venus	0.91
3	Mars	0.38
4	Jupiter	2.53
5	Saturn	1.07
6	Uranus	0.89
7	Neptune	1.14

If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.
"""
#destination weight=Earth weight × relative gravity
#destination weight=Earth weight × relative gravity

earth_weight = float(input("What is your Earth Weight ? \n"))
planet_number = int(input("What is your planet number ? \n"))

# Define the data first (Good practice to keep data at the top)
relative_gravity = [0.38 , 0.91 , 0.38 , 2.53 , 1.07 , 0.89 , 1.14]

if 1 <= planet_number <= 7:
    # Only run this logic if the number is SAFE
    gravity = relative_gravity[planet_number - 1]
    destination_weight = earth_weight * gravity
    
    print("Relative gravity:", gravity)
    print("Your weight at destination planet:", destination_weight)

else:
    # This runs if the number is bad
    print("Invalid Planet number")