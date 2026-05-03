# Odd or Even Program

# Method 1: Using modulus
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Method 2: Using ternary
num = int(input("Enter another number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(num, "is", result)

# Special case: 0 is even
# Negative numbers work too: -7 % 2 = 1 (odd), -8 % 2 = 0 (even)
