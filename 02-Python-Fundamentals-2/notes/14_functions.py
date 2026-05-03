# Functions in Python
# A function is a reusable block of code that performs a specific task

# --- Why functions? ---
# 1. Avoid repeating code (DRY - Don't Repeat Yourself)
# 2. Break big problems into smaller pieces
# 3. Makes code organized and readable
# 4. Easy to debug and test

# --- Defining a function ---
def greet():
    print("Hello! Welcome to Python.")

# --- Calling a function ---
greet()
greet()  # can call multiple times

# --- Function with parameters ---
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Dev")
greet_user("Shah")

# --- Function with return value ---
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum:", result)

# --- Multiple parameters ---
def full_name(first, last):
    return f"{first} {last}"

print(full_name("Devansh", "Shah"))

# --- Default parameters ---
def power(base, exp=2):  # exp defaults to 2 if not provided
    return base ** exp

print(power(5))      # 25 (5^2)
print(power(5, 3))   # 125 (5^3)

# --- Return multiple values ---
def min_max(a, b, c):
    return min(a, b, c), max(a, b, c)

smallest, largest = min_max(10, 5, 20)
print(f"Min: {smallest}, Max: {largest}")

# --- Scope: Local vs Global ---
x = 100  # global variable

def my_func():
    x = 50  # local variable (different from global x)
    print("Inside function:", x)

my_func()               # 50
print("Outside function:", x)  # 100 (unchanged)

# --- Using global keyword ---
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print("Counter:", counter)  # 2
