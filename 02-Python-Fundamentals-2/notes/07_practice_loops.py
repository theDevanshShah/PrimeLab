# Practice Examples — Loops

# 1. Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()  # newline

# 2. Print even numbers from 2 to 20
i = 2
while i <= 20:
    print(i, end=" ")
    i += 2
print()

# 3. Sum of digits of a number
num = int(input("Enter a number: "))
total = 0
temp = num

while temp > 0:
    total += temp % 10
    temp //= 10

print("Sum of digits of", num, "=", total)

# 4. Check if a number is palindrome
num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

if original == rev:
    print(original, "is a Palindrome")
else:
    print(original, "is NOT a Palindrome")

# 5. Power of a number (without **)
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
i = 1

while i <= exp:
    result *= base
    i += 1

print(f"{base}^{exp} = {result}")
