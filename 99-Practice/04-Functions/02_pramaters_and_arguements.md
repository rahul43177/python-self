# Parameters and Arguments

### 1. Parameters : 
- Parameters are just a fancy word for input. They are variables that a functions takes in. 
- They go inside the parentheses in the function definition and are used inside the function.
- For example, suppose we define and call a `happy_birthday()` function like so:

```python
def happy_birthday():
  print('Happy birthday to you')
  print('Happy birthday to you')
  print('Happy birthday dear friend')
  print('Happy birthday to you')

happy_birthday()
```

But we can send a name also in the function -- input to the function that would be parameter 
```py
def happy_birthday(name):
  print('Happy birthday to you')
  print('Happy birthday to you')
  print('Happy birthday dear ' + name )
  print('Happy birthday to you')
```

`name` this is function parameter here. 




### 2. Arguements : 
An argument is the value sent to the function when the function is called.
```python 
happy_birthday('Lillian')
```

Here the **Lillian** is Arguement. 


### Difference between Parameter and Arguement : 
- The parameter is the variable listed inside the parenthesis in the function definition (when we define the function).
- The argument is the value sent to the function (when we call the function).

