# Variables in Python
# A variable is like a container that stores data

# Creating variables (no need to declare type - Python figures it out!)
name = "Dev"
age = 21
height = 5.9
is_student = True

print(name)
print(age)
print(height)
print(is_student)

# Variable naming rules:
# 1. Can contain letters, numbers, underscores
# 2. Must start with a letter or underscore (not a number)
# 3. Case-sensitive (name and Name are different)
# 4. Cannot use reserved keywords (if, else, for, etc.)

# Valid variable names
my_name = "Dev"
_age = 21
name2 = "Shah"

# Invalid variable names (will cause error if uncommented)
# 2name = "Dev"       # cannot start with number
# my-name = "Dev"     # cannot use hyphen
# class = "AI"        # cannot use keywords

# Reassigning variables
x = 10
print("x =", x)
x = 20
print("x =", x)  # value updated to 20

# Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)

# Same value to multiple variables
x = y = z = 100
print(x, y, z)

# Swapping variables (Python makes it easy!)
a = 5
b = 10
print("Before swap:", a, b)
a, b = b, a
print("After swap:", a, b)

# type() function - check what type a variable is
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>

# id() function - check memory address of a variable
print(id(name))
print(id(age))

x = 5
y = 10
print("Before swap:", x, y)
z = y
y = x
x = z
print("After swap:", x, y)