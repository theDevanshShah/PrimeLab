# Data Types in Python
# Python has several built-in data types

# 1. int - Integer (whole numbers)
age = 21
negative_num = -5
big_num = 1000000
print("int:", age, type(age))

# 2. float - Floating point (decimal numbers)
height = 5.9
pi = 3.14159
negative_float = -2.5
print("float:", height, type(height))

# 3. str - String (text)
name = "Dev"
greeting = 'Hello World'
empty_string = ""
print("str:", name, type(name))

# 4. bool - Boolean (True or False)
is_student = True
is_graduated = False
print("bool:", is_student, type(is_student))

# 5. NoneType - represents absence of value
result = None
print("None:", result, type(result))

# 6. complex - Complex numbers (used in advanced math)
z = 3 + 4j
print("complex:", z, type(z))

# --- Type Conversion (Casting) ---

# int to float
x = 10
print(float(x))  # 10.0

# float to int (truncates decimal part)
y = 3.99
print(int(y))  # 3 (not rounded, just removes decimal)

# int/float to string
age = 21
print("I am " + str(age) + " years old")

# string to int/float
num_str = "100"
print(int(num_str) + 50)    # 150
print(float(num_str) + 0.5) # 100.5

# --- Taking Input from User ---
# input() always returns a string!

# name = input("Enter your name: ")
# print("Hello", name)

# age = int(input("Enter your age: "))
# print("Next year you'll be", age + 1)

# --- Checking Data Types ---
print(isinstance(42, int))       # True
print(isinstance(3.14, float))   # True
print(isinstance("Dev", str))    # True
print(isinstance(True, bool))    # True
