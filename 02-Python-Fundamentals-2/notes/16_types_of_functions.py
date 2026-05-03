# Types of Functions in Python

# --- 1. Built-in Functions ---
# Already provided by Python — no need to define
print(len("hello"))       # 5
print(max(10, 20, 30))    # 30
print(min(10, 20, 30))    # 10
print(sum([1, 2, 3, 4]))  # 10
print(abs(-42))           # 42
print(round(3.7))         # 4
print(type(42))           # <class 'int'>

# --- 2. User-defined Functions ---
# Functions you create yourself
def square(n):
    return n ** 2

print(square(5))  # 25

# --- 3. Functions with no return (void functions) ---
# They perform an action but return None
def say_hello(name):
    print(f"Hello, {name}!")

result = say_hello("Dev")
print(result)  # None

# --- 4. Functions with multiple return values ---
def calculate(a, b):
    return a + b, a - b, a * b

add, sub, mul = calculate(10, 5)
print(f"Add: {add}, Sub: {sub}, Mul: {mul}")

# --- 5. Recursive Functions ---
# A function that calls itself
def countdown(n):
    if n <= 0:
        print("Go!")
        return
    print(n)
    countdown(n - 1)

countdown(5)
