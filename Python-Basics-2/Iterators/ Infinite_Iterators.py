from itertools import count 

# create an infinite iterator that start the count from 1 and continue indefinitely 


infinite_iterator = count(1)

for i in range(10):
    print(next(infinite_iterator))