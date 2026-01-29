"""
Comprehensions :
This is a specialized python syntax for creating new => New Lists , Dictionaries  or sets  from existing ones.
They are faster than traditional for loops and much more concise.
"""

# Imagine you've queried the database and got a list of dictionary items representing stock.
raw_inventory = [
    {"article": "A1", "stock": 50},
    {"article": "B2", "stock": 0},
    {"article": "C3", "stock": 12},
]

# now we just want names of the article that are actually in stock (stock > 0)
# we can do it in one line using :

# in_stock_article_names = [item["article"] for item in raw_inventory if item["stock"] > 0 ]
"""
SYNTAX :  [expression for item in iterable if condition]
in_stock_names = [item["article"] for item in raw_inventory if item["stock"] > 0]
Output: ["A1", "C3"]
"""

in_stock = [item["article"] for item in raw_inventory if item["stock"] > 0 ]
print(in_stock)

stock_for_a1 = [item["stock"] for item in raw_inventory if item["article"] == "A1"]

print(stock_for_a1)

"""
['A1', 'C3']
[50]
"""
