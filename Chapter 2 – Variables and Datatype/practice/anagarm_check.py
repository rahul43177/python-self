def palindrome_check(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    return False


string1 = "aaaaarc"
string2 = "car"

print("The string is palindrome" if palindrome_check(string1 , string2) else "The string is not palindrome")