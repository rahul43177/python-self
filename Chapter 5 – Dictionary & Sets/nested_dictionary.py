# Nested dictionary
people = {
    "person1": {
        "name": "Alice",
        "age": 30
    },
    "person2": {
        "name": "Bob",
        "age": 25
    }
}

person1Name = people["person1"]["name"]
print(person1Name)
# Output: Alice
