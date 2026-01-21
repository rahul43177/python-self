# Intro to Lambda

Along the way while learning Python, you have probably encountered times when you wished if there was an easier way to write functions, especially the shorter ones - sometimes. If that’s the case, you're in luck.

In Python, lambdas provide a quick way to define small functions. Functions are blocks of reusable code, allowing you to organize your program effectively. They take inputs, perform a task, and return a result. As a beginner, mastering them can open up new possibilities for concise and readable code.

# The Function With No Name

Lambda functions (also known as anonymous functions) are concise functions defined without a name. They are often used for short-lived tasks where a full function definition might seem verbose or unneeded.

The syntax for lambda functions is as follows:

```pycon
lambda arguments: expression
```


First, we use the reserved lambda keyword to begin defining the function. Then, we can use one or more arguments (separated by commas), followed by a : colon. On the other side of the colon is the expression that may use the arguments to produce an output.

Here's an example of a regular function that adds numbers, and is assigned to a variable:
```python
def double(x):
  return x * 2
```

And here's how you can write it as a **lambda function**:
```python
double = lambda x: x * 2
print(double(4))
# Output: 8
```


Although lambda functions are anonymous, they can be assigned to named variables and then used later with the variable name.