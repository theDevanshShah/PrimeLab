# Sum of N Numbers

# Method 1: Using for loop
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"Sum of first {n} numbers = {total}")

# Method 2: Using while loop
n = int(input("\nEnter N: "))
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(f"Sum of first {n} numbers = {total}")

# Method 3: Using formula (Gauss's trick)
# Sum = n * (n + 1) / 2
n = int(input("\nEnter N: "))
total = n * (n + 1) // 2
print(f"Sum of first {n} numbers = {total}")

# --- Sum of squares ---
n = int(input("\nEnter N for sum of squares: "))
total = 0

for i in range(1, n + 1):
    total += i ** 2

print(f"Sum of squares of first {n} numbers = {total}")
