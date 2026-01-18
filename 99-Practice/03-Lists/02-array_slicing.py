
## SLICING 
"""
Is there a way to get more than just one individual item? Yep! It's called slicing.

Slicing is where we can access certain parts of a sequence.

Instead of accessing an item using a single index like name[index], we can get multiple items by specifying where to start and where to end the range like name[start : end].
"""

vowels = ['a' , 'e' , 'i' , 'o' , 'u']
        #  0.    1.    2.    3.     4 
ei_array = (vowels[1:3]) # -> starts from 1 index and goes till 3-1 - 2 
#it should e and i -> 1 and 2 index 

print(vowels[0:3]) 
print(vowels[2:])





