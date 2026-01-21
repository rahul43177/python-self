"""
Count down from 10 to 1 and print a New Year message.

This module prints the numbers 10 through 1, each on its own line,
using a for loop with range(start, stop, step), then prints
"Happy New Year! 🥳".

Note: range(10, 0, -1) uses an exclusive stop value (0), so the
iteration stops after yielding 1 — it stops at 1 (0 is not included).
Instructions
Ring in the New Year! A New Year's Eve party doesn't feel complete without a countdown from 10 to 1.
Use a for loop that counts down by using the "step" value in range().
Inside the loop, print the numbers from 10 to 1, each on its own line.
When the loop finishes the countdown, print this exact string Happy New Year! 🥳.
The output should look like this:
10
9
8
7
6
5
4
3
2
1
Happy New Year! 🥳
Counting down from 10 to 1 on each line and then a Happy New Year message at the end.
Note: Feel free to end your message with any emoji you want!
"""

for i in range(10 , 0 , - 1) :
    print(i) 

print("Happy New Year! 🥳")



"""
Hint

The range() function has start, stop, step parameters.

It can work in unison with a for loop:
            start stop step
for n in range(3, 0, -1): 
  print(n)

This will print out:

3
2
1

Make sure to output the message at the end.
"""