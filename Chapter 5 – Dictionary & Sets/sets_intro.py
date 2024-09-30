fruits = {"apple" , "banana" , "banana" , "pineapple"}
print(fruits)
print(type(fruits))


# Adding and Removing Items
# You can add an item to a set using the add() method and remove an item using the remove() or discard() method.
# Adding an item
fruits.add("orange")

# Removing an item
fruits.remove("banana")

# Using discard() method (does not raise an error if the item does not exist)
fruits.discard("banana")

fruits.add("watermelon")
print(fruits)


# Using set() function
numbers = [1,1,1,1,1,2,3,4,5,6]
number = [1,2,3,4]
unique_numbers = set(number)
print(unique_numbers) 

if len(unique_numbers) == len(number):
    print("There are no duplicates in the numbers")
else :
    print("There are some duplicates in the numbers")



