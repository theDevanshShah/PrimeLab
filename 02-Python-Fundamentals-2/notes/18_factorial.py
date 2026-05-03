# Factorial of N
# n! = n × (n-1) × (n-2) × ... × 2 × 1
# Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

# Method 1: Using for loop
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))
print(f"{n}! = {factorial_loop(n)}")

# Method 2: Using while loop
def factorial_while(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(f"Using while: {factorial_while(5)}")  # 120

# Method 3: Using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:  # base case
        return 1
    return n * factorial_recursive(n - 1)  # recursive case

print(f"Using recursion: {factorial_recursive(5)}")  # 120

# How recursion works for factorial(5):
# factorial(5) = 5 * factorial(4)
# factorial(4) = 4 * factorial(3)
# factorial(3) = 3 * factorial(2)
# factorial(2) = 2 * factorial(1)
# factorial(1) = 1 (base case!)
# Now it unwinds: 2*1=2, 3*2=6, 4*6=24, 5*24=120

# Method 4: Using math module
import math
print(f"Using math: {math.factorial(5)}")  # 120

# Edge case: 0! = 1 (by definition)
print(f"0! = {factorial_loop(0)}")  # 1
