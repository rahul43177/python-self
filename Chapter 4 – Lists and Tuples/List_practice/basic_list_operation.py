"""
Create a list of your favorite fruits.
Add a new fruit to the list.
Remove a fruit from the list.
Find the length of the list.
Check if a specific fruit is in the list.
"""

fruits = ["Apple" , "Mango" , "Banana" , "Watermelon"]

fruits.append("Pineapple")

fruits.pop() #removed the last element
fruits.pop(0) #removed the fruit from the 0th index

print(fruits)
print("length of the fruits" , len(fruits))

