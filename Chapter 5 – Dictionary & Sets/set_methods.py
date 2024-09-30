""" 
Here are some useful set methods:
add(): Adds an element to the set.
remove(): Removes an element from the set. Raises a KeyError if the element is not found.
discard(): Removes an element from the set if it is a member. If the element is not a member, do nothing.
pop(): Removes and returns an arbitrary set element. Raises KeyError if the set is empty.
clear(): Removes all elements from the set.
"""
fruits = {"Apple" , "Mango" , "Pineapple", "Watermelon"}

fruits.add("Orange")

print(fruits)
fruits.remove("Orange")
fruits.discard("Watermelon")
print(fruits)


fruits.clear()
print(fruits)
