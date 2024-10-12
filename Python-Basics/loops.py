fruits = ["Pineapple", "Watermelon", "Apple", "Orange", "Guava"]
suffixes = {1: 'st', 2: 'nd', 3: 'rd'}

for i, fruit in enumerate(fruits, start=1):
    suffix = suffixes.get(i if i < 20 else i % 10, 'th')
    print(f"The {i}{suffix} fruit is -> {fruit}")
