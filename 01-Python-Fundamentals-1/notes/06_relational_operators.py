# Relational (Comparison) Operators in Python
# They compare two values and return True or False

a = 10
b = 20

# Equal to
print("a == b:", a == b)   # False

# Not equal to
print("a != b:", a != b)   # True

# Greater than
print("a > b:", a > b)     # False

# Less than
print("a < b:", a < b)     # True

# Greater than or equal to
print("a >= b:", a >= b)   # False

# Less than or equal to
print("a <= b:", a <= b)   # True

# --- Comparing same values ---
x = 10
y = 10
print(x == y)   # True
print(x >= y)   # True (equal counts!)
print(x <= y)   # True

# --- Comparing strings (alphabetical / lexicographic order) ---
print("apple" < "banana")   # True  (a comes before b)
print("cat" > "car")        # True  (t > r)
print("abc" == "abc")       # True
print("A" < "a")            # True  (uppercase comes before lowercase in ASCII)

# --- Comparing different types ---
print(10 == 10.0)   # True  (int and float can be compared)
print(1 == True)     # True  (True is 1)
print(0 == False)    # True  (False is 0)

# --- Chained comparisons (Python special!) ---
age = 25
print(18 <= age <= 60)  # True (checks if age is between 18 and 60)

x = 5
print(1 < x < 10)      # True
print(1 < x < 3)       # False

# --- Common mistake ---
# = is assignment, == is comparison
# x = 5   (assigns 5 to x)
# x == 5  (checks if x equals 5)

# --- Practical example ---
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")
