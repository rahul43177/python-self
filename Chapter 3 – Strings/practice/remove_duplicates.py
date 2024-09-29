def remove_duplicates(string) :
    result = ""
    for char in string :
        if char not in result:
            result += char
    return result

str1 = "aaaaaaa"
str2 = "bbbaaaa"
name = "Rahul Mishra"

print(remove_duplicates(name))
