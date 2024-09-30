""" 
- Create a dictionary named `inventory` with items and their quantities.
- Use the `get` method to retrieve the quantity of an item that might not exist in the dictionary.
- Use the `setdefault` method to add a new item with a default quantity if it doesn't already exist.
- Use the `pop` method to remove an item from the dictionary and print the removed item.
- Use the `items` method to iterate over the dictionary and print each item and its quantity.
"""

inventory = {
    "soap" : 3 , 
    "brush" : 2 , 
    "pencil" : 5 ,
    "chocolate" : 10
}

grape_quantity = inventory.get("grapes" , 0) #if that key is not found , 0 is the default value which will be displayed , it can be anything like below 

guava_quantity = inventory.get("guava" , "not found") #here the default value is -> not found

print(f"quantity of grapes : {grape_quantity}")

inventory.setdefault("grapes" , 10)
print(inventory)