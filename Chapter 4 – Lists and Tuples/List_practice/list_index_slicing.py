numbers = [1,2,3,4,5,6,7,8,9,10]

#access first and last element of the list 

first_number = numbers[0]
last_number = numbers[-1]

print(f"The first number is -> {first_number}")
print(f"The last number is -> {last_number}")

first_five_numbers = numbers[:5]
print(f"The first five number are -> {first_five_numbers}")

last_three_numbers = numbers[-3:]
print(f"The last three numbers are -> {last_three_numbers}")

reversed_list = numbers[::-1]
print(f"The reversed list is -> {reversed_list}")
