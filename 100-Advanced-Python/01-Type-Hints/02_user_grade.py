# Write a function signature (just the first line) for a function named get_user_grades that:
# Takes a variable user_id (an integer).
# Returns a Dictionary where the Keys are strings (subject names) and the Values are integers (scores).

grades_database = [
    {
        "user_id" : 1,
        "grades" : {
            "maths" : 65 ,
            "economics" : 77 ,
            "english" : 88 ,
            "chemistry" : 33
        }
    }
]

#
def get_user_grades(user_id : int) -> dict[str,int] | None :
    return grades_database[0]["grades"]


print(get_user_grades(1))

