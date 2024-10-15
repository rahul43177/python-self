## IMPLICIT TYPE CASTING
#converting integer to float
number = 12  #int
float = 23.2 #float

new_number = number + float
print("The new number is ->" , new_number)
print("Type of the new number is ->" , type(new_number))

## EXPLICIT TYPE CASTING
# we change it 

my_float = 3.14  # Renamed variable
string_number = "12.2"
float_type_casted = float(string_number)  # Now this works correctly
