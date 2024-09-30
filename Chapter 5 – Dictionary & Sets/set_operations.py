""" 
Sets support mathematical operations like union, intersection, difference, and symmetric difference.
- union(): Returns a set containing all elements from both sets.
-intersection(): Returns a set containing only the elements that are common to both sets.
-difference(): Returns a set containing elements that are in the first set but not in the second set.
-symmetric_difference(): Returns a set containing elements that are in either of the sets, but not in both.
"""

set1 = {1,2,3,4,5,9}
set2 = {6,7,8,9,10}
union_set = set1.union(set2) #returns all the elements from both sets
print(union_set)

intersection_set = set1.intersection(set2) #Returns a set containing only the elements that are common to both sets.
intersection_set2 = set2.intersection(set1) #same result
print(intersection_set) 
print(intersection_set2)

difference_set = set1.difference(set2) #this will give me set1 
difference_set2 = set2.difference(set1) #this will give me set2 
print(difference_set2)
print(difference_set)

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)
