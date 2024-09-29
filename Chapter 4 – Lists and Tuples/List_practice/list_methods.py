"""
List Methods

Use the append(), extend(), insert(), remove(), and pop() methods on a list and observe the changes.
"""
# Create a list of numbers and sort it in ascending order.
list = [1,4,5,2,3]

# Create a list of strings and sort it in descending order.
string_list = ["Rahul" , "Anshul" , "Muskan" , "Jena"]

list.sort()
print(list)
string_list.sort()
print(string_list)
# Use the append(), extend(), insert(), remove(), and pop() methods on a list and observe the changes.
#append
list.append(6)
print(list)
#extend
list.extend([7,8,9,10])
print(list)
#insert at specific index
list.insert(0,0)
print(list)
#remove element at specific index
list.remove(10)
print(list)

