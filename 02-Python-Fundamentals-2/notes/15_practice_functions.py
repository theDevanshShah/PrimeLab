# Practice Examples — Functions

# 1. Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is Prime")
else:
    print(f"{num} is NOT Prime")

# 2. Find GCD (Greatest Common Divisor) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("GCD of 48 and 18:", gcd(48, 18))  # 6

# 3. Check if a string is a palindrome
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

word = input("\nEnter a word: ")
if is_palindrome(word):
    print(f"'{word}' is a Palindrome")
else:
    print(f"'{word}' is NOT a Palindrome")

# 4. Temperature converter
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

print("\n30°C =", celsius_to_fahrenheit(30), "°F")
print("86°F =", fahrenheit_to_celsius(86), "°C")

# 5. Count digits in a number
def count_digits(n):
    count = 0
    n = abs(n)  # handle negative numbers
    if n == 0:
        return 1
    while n > 0:
        n //= 10
        count += 1
    return count

print("\nDigits in 98765:", count_digits(98765))  # 5
