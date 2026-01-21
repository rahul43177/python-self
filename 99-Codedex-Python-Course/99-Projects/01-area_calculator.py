import math
print(""" 
==================
Area Calculator 📐
==================
""")

print("Select which area you would like to find!!")
shape = int(input(""" 
1) Triangle 
2) Rectangle 
3) Square 
4) Circle
5) Quit

Which Shape : 
"""))

area = 0 
#triange
if shape == 1 :
    height = int(input("Please enter the height : "))
    base = int(input("Please enter the base : "))

    area = (height * base) / 2

#reactangle 
if shape == 2 : 
    length = int(input("Please enter the length : "))
    width = int(input("Please enter the width : "))

    area = length * width 

#sqaure
if shape == 3 : 
    side = int(input("Please enter the side : "))
    area = side**2 


if shape == 4 :
    radius = int(input("Please enter the radius : "))
    area = math.pi * (radius ** 2)

if shape == 5 :
    print("Bye Bye ! Take care")


if shape != 5 :
    print(f"The area is : {area}")