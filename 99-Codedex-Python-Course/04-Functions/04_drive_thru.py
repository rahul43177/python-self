"""
Define a get_item() function that takes in one parameter, the number of the item you want to order, and returns the name of that item!

For example, if you called the function with:

    Argument value 1, it could return '🍔 Cheeseburger'.
    Argument value 2, it could return '🍟 Fries'.
    Argument value 3, it could return '🥤 Soda'.
    Argument value 4, it could return '🍦 Ice Cream'.
    Argument value 5, it could return '🍪 Cookie'.

Make sure to call this function a few times to make sure that it works!

Lastly, let's do the following:

    Create a welcome menu and put that in a welcome() function.
    Create a main program that takes in user input with input().
"""
from time import sleep
import time
fast_food = [
    '🍔 Cheeseburger',
    '🍔 Double Cheeseburger',
    '🍗 Fried Chicken',
    '🍗 Chicken Wings',
    '🍟 Fries',
    '🧀 Cheese Fries',
    '🌭 Hot Dog',
    '🥪 Chicken Sandwich',
    '🥪 Veg Sandwich',
    '🌮 Taco',
    '🌯 Burrito',
    '🍕 Cheese Pizza',
    '🍕 Pepperoni Pizza',
    '🍕 Veggie Pizza',
    '🍕 Chicken Pizza',
    '🥓 Bacon Burger',
    '🥩 Steak Burger',
    '🍖 BBQ Ribs',
    '🍤 Chicken Nuggets',
    '🍤 Popcorn Chicken',
    '🥨 Pretzel',
    '🥯 Bagel',
    '🍩 Donut',
    '🧁 Cupcake',
    '🍰 Cake Slice',
    '🍦 Ice Cream',
    '🍨 Sundae',
    '🍪 Cookie',
    '🍫 Brownie',
    '🥤 Soda',
    '🧃 Juice',
    '☕ Coffee',
    '🧋 Milkshake',
    '🧂 Nachos',
    '🧀 Cheese Nachos',
    '🥗 Coleslaw',
    '🍜 Ramen Cup',
    '🍝 Pasta',
    '🍚 Fried Rice',
    '🍔 Slider Burger',
    '🌽 Corn Dog',
    '🍳 Breakfast Sandwich',
    '🥞 Pancakes',
    '🧇 Waffles'
]

def welcome() :
    print(f"Hi sir , Welcome to my shop of tasty fast foods!")
    print(f"Here is our quick menu of the items we have for today!")
    print("="*50)
    for i in range(len(fast_food)) :
        print(f"item : {i+1} -- {fast_food[i]}")
    print("="*50)
    print("\n")
    print("PLease take your time and choose sir.")
    return

def user_input():
    time.sleep(4)
    item_number = int(input("What would like to have sir? \n"))
    print(f"Thank you sir , we got your order!")
    return item_number
def get_item(item_number):
    time.sleep(3)
    print("Your order is getting prepared sir , Thank you for your patience!!")
    time.sleep(3)
    return fast_food[item_number-1]



def main() :
    welcome()
    item_number = user_input()
    item = get_item(item_number)
    print(f"Sir/Mam , Here is your food : {item}")
    print("Please visit again!")


main()