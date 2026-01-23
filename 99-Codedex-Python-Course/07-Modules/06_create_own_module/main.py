import datetime , bday_messages , math

today = datetime.date.today()

next_birthday = datetime.date(2026 , 10 , 11)

days_away = (next_birthday - today).days

if today == next_birthday:
    print(bday_messages.random_message)
else :
    print(f"My next birthday is {days_away} days away!")

