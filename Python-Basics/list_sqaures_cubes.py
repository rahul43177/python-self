#find sqaures in the array till 20

sqaures_till_20 = [x**2 for x in range(1,21)]

for index , value in enumerate(sqaures_till_20 , start = 1):
    print(f"The sqaure of {index} -> {value}")

#find cubes in the array till 20

cubes = [x*x*x for x in range(1,21)]
for i , v in enumerate(cubes , start=1):
    print(f"The cube of {i} -> {v}")

    
