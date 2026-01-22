"""
# Use Cases

Lambdas are particularly useful in situations where a small, one-time-use function is needed.

When using functions like map() and filter() to perform operations on collections like lists, they require a function as one of their parameters!

This is where lambda functions come into play:

numbers = [1, 2, 3, 4, 5]

tripled_numbers = list(map(lambda x: x * 3, numbers))

odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))

print(tripled_numbers)  # Output: [3, 6, 9, 12, 15]
print(odd_numbers)      # Output: [1, 3, 5]

And just like that, we were able to include a single-line lambda function in each example above. lambda x: x * 2 and also lambda x: x % 2 == 1 really did a lot of work!

For more information about the functions used:

    map()
    filter()
"""
from dotenv import find_dotenv

#MAP
# SYNTAX : map(function, iterable/array/list)

## USING normal function
# a function to call
def find_square(n) :
    return n**2

#iteratable / list
numbers = [1,2,3,4,5]


# SYNTAX : map(function, iterable/array/list)
squares = list(map(find_square , numbers))

print(squares)

## USING lambda Function

squares_result = list(map(lambda num : num ** 2 , numbers))
                #list map   lambda function        list to iterate
print(squares_result)




# FILTER Function
#SYNTAX : filter(function, iterable)

def is_even(n) :
    return n%2 == 0

## This will return boolean -- and if true -- we pick it and save it in our array otherwise filter it out

evens = list(filter(is_even , numbers ))
print(evens)

## using lambda function

evens_using_lambda = list(filter(lambda num : num % 2 == 0 , numbers))
print(evens_using_lambda)

