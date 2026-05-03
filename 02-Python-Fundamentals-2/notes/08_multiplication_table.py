# Multiplication Table of N

# Method 1: Using while loop
n = int(input("Enter a number: "))
i = 1

print(f"\n--- Multiplication Table of {n} ---")
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

# Method 2: Using for loop
n = int(input("\nEnter another number: "))

print(f"\n--- Multiplication Table of {n} ---")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Method 3: Custom range
n = int(input("\nEnter number: "))
start = int(input("From: "))
end = int(input("To: "))

print(f"\n--- Table of {n} from {start} to {end} ---")
for i in range(start, end + 1):
    print(f"{n} x {i} = {n * i}")
