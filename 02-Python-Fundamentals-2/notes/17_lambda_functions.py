# Lambda Functions in Python
# Small anonymous functions defined in one line

# --- Regular function vs Lambda ---

# Regular function
def square(x):
    return x ** 2

# Same thing as lambda
square_lambda = lambda x: x ** 2

print(square(5))         # 25
print(square_lambda(5))  # 25

# --- Syntax ---
# lambda arguments: expression
# - No name needed (anonymous)
# - Single expression only (no if-else blocks, no loops)
# - Returns the result automatically

# --- Examples ---

# Add two numbers
add = lambda a, b: a + b
print(add(3, 7))  # 10

# Check even/odd
is_even = lambda n: n % 2 == 0
print(is_even(4))   # True
print(is_even(7))   # False

# Max of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # 20

# --- Lambda with built-in functions ---

# sort a list of tuples by second element
students = [("Dev", 85), ("Alice", 92), ("Bob", 78)]
students.sort(key=lambda x: x[1])
print(students)  # sorted by marks

# filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)  # [2, 4, 6, 8, 10]

# square all numbers using map
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)  # [1, 4, 9, 16, 25, ...]

# --- When to use lambda ---
# - Short, throwaway functions (used once)
# - As arguments to functions like sort(), filter(), map()
# - NOT for complex logic — use def for that
