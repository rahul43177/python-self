# { key: value for item in iterable if condition }   # dict
# { expression for item in iterable if condition }   # set

users = {
    "u1": {"name": "Rahul", "age": 24, "active": True,  "role": "admin"},
    "u2": {"name": "Amit",  "age": 19, "active": False, "role": "user"},
    "u3": {"name": "Anshul",  "age": 27, "active": True,  "role": "user"},
    "u4": {"name": "Ayush",  "age": 22, "active": True,  "role": "user"},
}



# {key : value for item in iterable if condition }

active_user_map = {
    user_info["name"]
    for user_id , user_info in users.items()
    if user_info["active"] == True
}

user_status = {
    user_id : (
        "ACTIVE" if user_info["active"] else "INACTIVE"
    )
    for user_id , user_info in users.items()
}

print(user_status)

