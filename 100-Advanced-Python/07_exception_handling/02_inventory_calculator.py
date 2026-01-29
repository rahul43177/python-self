"""
Fresh Problem: The Inventory Calculator 🧮

We are going to build a tool that calculates the price per unit for an inventory shipment.

The Scenario: You have a function that takes total_cost and quantity. However, real-world data is messy—sometimes quantity might be zero or even a string!
The Task: Write a function calculate_unit_price(total_cost, quantity) that uses try...except to handle these specific errors:
    ZeroDivisionError: If quantity is 0 (we can't divide by zero! 🚫).
    TypeError: If someone passes a string instead of a number.
Your Goal: If an error occurs, the function should return 0 and print a helpful message. If it succeeds, it should return the calculated price.
What would the try block look like for this calculation? 🕵️‍♂️

"""

def calculate_unit_price(total_cost , quantity):
    try :
        price = total_cost / quantity
    except ZeroDivisionError :
        print("We can't divide by zero!")
        return 0
    except TypeError :
        print("The type can't be string")
        return 0

    return price  