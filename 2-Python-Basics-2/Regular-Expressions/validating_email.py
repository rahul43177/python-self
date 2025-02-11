import re 

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern , email) is not None


email_address = "rahul4317@gmail.com"
valid = is_valid_email(email_address)
if valid : 
    print(f"The {email_address} is valid")
else :
    print(f"The {email_address} is not valid")

    

