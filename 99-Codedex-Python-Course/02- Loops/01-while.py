pin = input("Please enter your ATM PIN !")

while pin != "1234" : 
    pin = input("Wrong PIN, please try again ! \n")
    
    if pin == "1234" : 
        print("PIN accepted, you can proceed !")
