"""
Create a todo.py program that will define a todo list that contains the following items:

    '🏦 Get quarters.'
    '🧺 Do laundry.'
    '🌳 Take a walk.'
    '💈 Get a haircut.'
    '🍵 Make some tea.'
    '💻 Complete Lists chapter.'
    '💖 Call mom.'
    '📺 Watch My Hero Academia.'

Print the first item and print the second item. What did you get?

Next, use slicing to print the third, fourth, and fifth items.

Try printing out the item at index 9 to see the IndexError before moving on.
"""


todo = ['🏦 Get quarters.', '🧺 Do laundry.', '🌳 Take a walk.', '💈 Get a haircut.', '🍵 Make some tea.', '💻 Complete Lists chapter.', '💖 Call mom.', '📺 Watch My Hero Academia.']

first_item = todo[0]
second_item = todo[1]
print(first_item)
print(second_item)
#I got : 🏦 Get quarters. for first item
#I got : 🧺 Do laundry. for second item 
# 3 4 5 

third_fourth_fifth = todo[2:5]
print(third_fourth_fifth)


#index error 
print(todo[9])