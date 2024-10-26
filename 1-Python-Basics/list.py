#creation of list 
array = [] #square bracket 
new_array = list() #using list class

#list comprehension
#short method to get the sqaure
# 1 , 10 => 1, 11
squares = [x*x for x in range(1,11)]
print("THE SQUARES")
for index , value in enumerate(squares, start=1):
    print(f"The sqaure of {index} => {value}")


cubes = [x**3 for x in range(1,11)]
print("\n")
print("THE CUBES")
for index , value in enumerate(cubes , start = 1):
    print(f"The cube of {index} => {value}")

new_list_list = []
for i in range(1,11):
    new_list_list.append(i**4)
for index , value in enumerate(new_list_list , start=1):
    print(f"The 4 times {index} : {value}")

print("First Method : ",2**4)
print("Second Method : ",2*2*2*2)

#List slicing 

list = [0,1,2,3,4,5]
sliced_list = list[1:3] # 1 to 3-1 -> 1 to 2 -> index 
print(sliced_list)
slided_list2 = list[::-1] #reverse a list
print(slided_list2)

new_array_array = [10,1,2,33,23,45,1,11]
new_array_array.sort()
new_array_array.sort(reverse=True)
print('➡ Python-Basics/list.py:39 new_array_array sorted:', new_array_array)
new_array_array.sort(reverse=False)
print('➡ Python-Basics/list.py:39 new_array_array sorted:', new_array_array)

find_unique = set(new_array_array)
unique_list = sorted(find_unique)
print('Unique elements as list:', unique_list)


my_set = {1,2,3,4,5,6,7,7}
print("the set" , set)

list_from_set = list(my_set)
print('➡ Python-Basics/list.py:53 list_from_set:', list_from_set)


