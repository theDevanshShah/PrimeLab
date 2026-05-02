# Keywords & Comments in Python

# --- COMMENTS ---
# Comments are notes for humans, Python ignores them

# This is a single-line comment

# Multi-line comments using # on each line
# This is line 1
# This is line 2
# This is line 3

"""
This is a multi-line string (docstring).
It can also be used as a multi-line comment.
Python won't execute this unless it's assigned to a variable.
"""

'''
You can also use single quotes
for multi-line strings/comments.
'''

# Why use comments?
# 1. Explain what your code does
# 2. Make code readable for others (and future you!)
# 3. Temporarily disable code (commenting out)

# print("This line won't run")  # commented out


# --- KEYWORDS ---
# Keywords are reserved words with special meaning in Python
# You CANNOT use them as variable names

# To see all keywords:
import keyword
print("Total keywords:", len(keyword.kwlist))
print("Keywords:", keyword.kwlist)

# Common keywords and what they do:

# 1. True, False, None - boolean and null values
x = True
y = False
z = None

# 2. and, or, not - logical operators
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 3. if, elif, else - conditional statements
age = 21
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# 4. for, while, break, continue - loops
for i in range(3):
    print(i)

# 5. def, return - functions
def greet(name):
    return "Hello " + name

print(greet("Dev"))

# 6. class - object-oriented programming
# 7. import, from, as - importing modules
# 8. try, except, finally - error handling
# 9. is, in - identity and membership
# 10. lambda - anonymous functions

# Check if a word is a keyword
print(keyword.iskeyword("if"))      # True
print(keyword.iskeyword("hello"))   # False

# --- IDENTIFIERS ---
# Identifiers are names given to variables, functions, classes, etc.
# Rules:
# 1. Can contain a-z, A-Z, 0-9, and _
# 2. Cannot start with a digit
# 3. Cannot be a keyword
# 4. Case-sensitive