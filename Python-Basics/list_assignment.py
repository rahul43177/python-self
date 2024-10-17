# EASY
# Create a list: Create a list fruits with the following elements: "apple", "banana", "cherry".
fruits = ["apples" , "banana" , "cherry"]


# Access an element: Given a list numbers = [1, 2, 3, 4, 5], how do you access the third element?
numbers = [1,2,3,4,5]
        #  0,1,2,3,4
third_element = numbers[2]
print("Third element:",third_element)

# List length: Write a Python expression to find the length of a list my_list.
my_list = [1,2,3,4,5,6]
print(f"Length of the list -> {len(my_list)}")


#MEDIUM
# Append an element: Given a list colors = ["red", "green", "blue"], how do you add the element "yellow" to the end of the list?
colors = ["red" , "green" ,"blue"]
colors.append("yellow")
print(colors) 
print(f"length of the colors -> {len(colors)}")

# Insert an element: Given a list numbers = [1, 2, 3, 4, 5], how do you insert the element 6 at the second position?
numbers = [1,2,3,4,5]
numbers.insert(1,6)
print(numbers)

# Remove an element: Given a list fruits = ["apple", "banana", "cherry", "banana"], how do you remove the first occurrence of "banana"?

fruits = ["apple" , "banana" , "cherry" , "banana"]
fruits.remove("banana")
print(fruits)

# CHALLENGING
# Reverse a list: Write a Python expression to reverse a list my_list.

my_list = [1,2,3,4,5]
reversed_list = my_list[::-1]
print("The reversed list" , reversed_list)
new_reverse = []