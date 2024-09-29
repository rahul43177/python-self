# 1. Create a list of squares of numbers from 1 to 10 using a list comprehension
sqaures = [x**2 for x in range(1,11)]
print(sqaures)

# 2. Create a list of even numbers from 1 to 20 using a list comprehension
even_numbers = [x for x in range(1,21) if x % 2 ==0]
print(even_numbers)

# 3. Create a list of the first letter of each word in a given list of words
words = ["apple", "banana", "cherry", "date"]
first_letter = [word[0] for word in words]
print(first_letter)

