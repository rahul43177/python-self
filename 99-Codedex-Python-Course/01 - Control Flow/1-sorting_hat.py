# """
# The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

#     🦁 Gryffindor
#     🦅 Ravenclaw
#     🦡 Hufflepuff
#     🐍 Slytherin

# Write a program that asks the user some questions with the int() and input() functions:

# Q1) Do you like Dawn or Dusk?
#     1) Dawn
#     2) Dusk

#     If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
#     Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
#     Else, output the message "Wrong input."

# Q2) When I’m dead, I want people to remember me as:
#     1) The Good
#     2) The Great
#     3) The Wise
#     4) The Bold

#     If the answer is 1, Hufflepuff +2.
#     Else if answer is 2, Slytherin +2.
#     Else if answer is 3, Ravenclaw +2.
#     Else if answer is 4, Gryffindor +2.
#     Else, output the message "Wrong input."

# Q3) Which kind of instrument most pleases your ear?
#     1) The violin
#     2) The trumpet
#     3) The piano
#     4) The drum

#     If the answer is 1, Slytherin +4.
#     Else if the answer is 2, Hufflepuff +4.
#     Else if the answer is 3, Ravenclaw +4.
#     Else if the answer is 4, Gryffindor +4.
#     Else, output "Wrong input."

# Lastly, print out the score for each house.

# Bonus: If you want to go further, see if you can figure out how to print out the house with the most points!
# """

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0


# question 1 : 
"""
Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

    If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
    Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
    Else, output the message "Wrong input."
"""
answer1 = int(input("Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk \n"))
if answer1 == 1 : 
    Gryffindor += 1
    Ravenclaw +=1 
elif answer1 == 2 : 
    Hufflepuff += 1
    Slytherin += 1


#question 2 
"""
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

    If the answer is 1, Hufflepuff +2.
    Else if answer is 2, Slytherin +2.
    Else if answer is 3, Ravenclaw +2.
    Else if answer is 4, Gryffindor +2.
    Else, output the message "Wrong input."
"""

answer2 = int(input("When I'm dead , I want people to remember me as : \n1.The Good \n2.The Great \n3.The Wise \n4.The Bold\n"))

if answer2 == 1 :
    Hufflepuff += 2
elif answer2 == 2 :
    Slytherin += 2
elif answer2 == 3 :
    Ravenclaw += 2
elif answer2 == 4 :
    Gryffindor += 2
else :
    print("Wrong Input")

"""
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

    If the answer is 1, Slytherin +4.
    Else if the answer is 2, Hufflepuff +4.
    Else if the answer is 3, Ravenclaw +4.
    Else if the answer is 4, Gryffindor +4.
    Else, output "Wrong input."
"""

answer3 = int(input("What kinf od instrument most pleases your ear ? \n1. The Violin \n2. The trumpet \n3. The piano \n4. The drum\n"))

if answer3 == 1 : 
    Slytherin  += 4
elif answer3 == 2 : 
    Hufflepuff  += 4
elif answer3 == 3 : 
    Ravenclaw  += 4
elif answer3 == 4 : 
    Gryffindor  += 4
else :
    print("Wrong input.")



print("Scores of each house:")
print("Gryffindor :" , Gryffindor)
print("Ravenclaw :", Ravenclaw)
print("Hufflepuff :", Hufflepuff)
print("Slytherin :", Slytherin)

houses_scores = {
    "Gryffindor" : Gryffindor ,
    "Ravenclaw" : Ravenclaw ,
    "Hufflepuff" : Hufflepuff ,
    "Slytherin" : Slytherin 
}

max_score = max(Gryffindor , Ravenclaw , Hufflepuff , Slytherin)

for house_name , score in houses_scores.items() :
    if score == max_score : 
        print(f"You belong to : {house_name}")

