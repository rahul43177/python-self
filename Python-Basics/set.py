# creating a list of numbers
numbers = [1,1,1,2,3,4,5,6,6,6,6]

# converting the list to a set
set1 = set(numbers)
print(set1) # prints {1, 2, 3, 4, 5, 6}

# creating a set of numbers
set2 = {1,5}

# union of two sets
print(set1|set2) # prints {1, 2, 3, 4, 5, 6}

# intersection of two sets
print(set1 & set2) # prints {1, 5}

# difference of two sets
print(set1 - set2) # prints {2, 3, 4, 6}

# symmetric difference of two sets
print(set1 ^ set2) # prints {2, 3, 4, 6}

print(set1)