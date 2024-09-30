#Unpacking of tuple
my_tuple = (1, "apple", 3.14)

a , b , c = my_tuple

print(a , b,c)

print(type(a))
print(type(b))
print(type(c))


# Unpacking a Tuple with 5 Elements
#rest operator
new_tuple = (10, 20, 30, 40, 50)

x , y , *new_rest= new_tuple
print(new_rest)

