# While Loop in Python
# Repeats a block of code as long as condition is True

# --- Basic while loop ---
count = 1
while count <= 5:
    print("Count:", count)
    count += 1  # IMPORTANT: without this, infinite loop!

# --- How it works ---
# 1. Check condition
# 2. If True → run the body
# 3. Go back to step 1
# 4. If False → exit the loop

# --- Sum of first N natural numbers ---
n = int(input("Enter N: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print("Sum of first", n, "numbers =", total)

# --- Counting digits in a number ---
num = int(input("Enter a number: "))
count = 0
temp = num

while temp > 0:
    temp //= 10
    count += 1

print("Number of digits in", num, "=", count)

# --- Reverse a number ---
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed:", rev)

# --- while with else (rarely used but good to know) ---
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed!")  # runs when condition becomes False naturally
