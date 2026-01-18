"""
You have a function find_email that takes a user_id (int).
If the user is found, it returns their email (a string).
If the user is NOT found, it returns None.

Your Task: Write the full function definition (just the logic stub is fine) using the modern | syntax for the return type.
"""
user_database = [
    {
        "user_id" : 1 ,
        "email" : "qa@gmail.com"
    } ,
    {
        "user_id" : 2 ,
        "email" : "test@test.com"
    }
]

def find_email(user_id : int) -> str | None :
    for user in user_database :
        if user["user_id"]== user_id :
            return user["email"]
    return None

print(find_email(3))
