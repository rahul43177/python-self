import mymodule #imported entire mymodule

from mymodule import greet #imported specific function from the mymodule module

name = "Rahul"
greeting = mymodule.greet(name)

new_name = "Muskan"
specific_greet = greet(new_name)

print(greeting)
print(specific_greet)

"""
This is a multiline comment  
"""

#this is a single line comment
