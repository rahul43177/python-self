import re 

#1 - re.match(): Checks for a match only at the beginning of the string.
def find_match_first():
    text = "Rahul Mishra is a good boy"
    pattern = r"Rahul Mishra"

    match = re.match(pattern , text)
    if match : 
        print("The sentence starts from Rahul Mishra")
    else :
        print("The sentence does not start from Rahul Mishra")

# 2 - re.search(): Searches the entire string for a match.

def search_regex():
    text = "I love coding"
    pattern = r"coding"

    search = re.search(pattern , text)
    if search : 
        print("we found it")
    else :
        print("We did not found it")

# search_regex()

# 3 - re.findall(): Returns a list of all matches in the string.

def find_all():
    text = "The quick brown fox jumps over the lazy dog quick quick"
    pattern = r"quick"
    
    matches = re.findall(pattern , text )
    print(matches) #returns the list with all the found elements

# find_all()

# 4. re.sub(): Replaces matches with a string.

def replace():
    sentence = "My favourite fruit is Apple"
    pattern_to_replace = r"Apple"
    replacement = r"Watermelon"

    new_replaced_string = re.sub(pattern_to_replace , replacement , sentence)
    print(new_replaced_string)

replace()


