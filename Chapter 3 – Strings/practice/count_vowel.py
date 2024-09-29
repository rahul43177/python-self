def count_vowels(s) :
    vowels = "aeiou"
    count = 0
    for char in s:
        lower_char = char.lower()
        if lower_char in vowels:
            count +=1 
    return count

name = "RAhul Mishra"
print(count_vowels(name))
            
    