# For Loop in Python
# Iterates over a sequence (list, string, range, etc.)

# --- Basic for loop ---
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# --- for with string ---
name = "Python"
for char in name:
    print(char, end=" ")
print()  # P y t h o n

# --- for with range ---
# range(stop) → 0 to stop-1
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# range(start, stop) → start to stop-1
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5
print()

# range(start, stop, step)
for i in range(0, 20, 3):
    print(i, end=" ")  # 0 3 6 9 12 15 18
print()

# --- Counting backwards ---
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1
print()

# --- for vs while ---
# Use for: when you know how many times to loop
# Use while: when you loop until a condition changes

# --- Nested for loops ---
# Print a pattern:
# * * *
# * * *
# * * *
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# --- Right triangle pattern ---
n = 5
for i in range(1, n + 1):
    print("* " * i)

# --- for with else ---
for i in range(5):
    print(i)
else:
    print("Loop finished!")  # runs if loop completes without break
