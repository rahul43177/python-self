# Tuples

Tuples are ordered collections that cannot be changed after creation.

This means that they are immutable, which means their values cannot change. They’re great for data that should stay the same, like coordinates or color values.

However, we can replace one tuple with another and have duplicates within a tuple.

Lists and tuples have a few things in common:

    They can store multiple items in a single variable.
    Their values are separated by commas.

However, tuples are created using ( ) parentheses. Here are two examples:

person = ('Kat', 24)
navy_blue = (0, 0, 128)

They are also defined without parentheses and their items can be a mix of any data type. They can have one or more items.

# valid tuple
t1 = ('hi',)

# valid tuple
t2 = 'hi',

# not a tuple
t3 = ('hi')

If there is only one item, make sure there is a comma , beside it.
# Creating and Accessing Tuples

For example, a DNA sequence would be stored as a tuple since it contains very important values that should not be changed and should not change when referenced without.

my_dna = ('GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT')

Because tuples are an ordered collection, we can access tuple items the same way we do with lists... using the index!

If we want to get the 3rd item in our my_dna tuple:

print(my_dna[2]) # Output: AGG

# Using Tuples

Tuples are also unpackable which allows us to easily turn them into variables. Most commonly, tuples are used as return values allowing us to easily work with large data sets.

full_name = ('Ada', 'Lovelace')

first_name = full_name[0]

print(first_name) # Output: Ada

Tuples can also be combined:

# Combining tuples
t1 = 'a',
t2 = 'b',
t3 = t1 + t2

print(t3)  # Output: ('a', 'b')
