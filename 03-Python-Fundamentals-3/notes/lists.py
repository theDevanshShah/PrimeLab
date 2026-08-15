"""
╔════════════════════════════════════════════════════════════════╗
║        LISTS IN PYTHON: A COMPLETE BEGINNER'S GUIDE           ║
║                                                                ║
║ Learn how to work with collections of data efficiently        ║
╚════════════════════════════════════════════════════════════════╝
"""

# ═══════════════════════════════════════════════════════════════
# PART 1: THE PROBLEM — Why do we need Lists?
# ═══════════════════════════════════════════════════════════════


print("=" * 60)
print("PART 1: Why Lists Matter")
print("=" * 60)

# Imagine you're tracking exam scores for 5 students...
# The OLD WAY (storing each value separately):

student_1 = 50
student_2 = 56
student_3 = 89
student_4 = 69
student_5 = 67

print("\nOLD WAY: 5 separate variables")
print(f"Student 1: {student_1}")
print(f"Student 2: {student_2}")
print(f"Student 3: {student_3}")
print(f"Student 4: {student_4}")
print(f"Student 5: {student_5}")

# What if you had 1000 students? 😱 This approach is TERRIBLE!
# → Imagine writing student_1000 = ... variable assignments!
# → How would you find the average of all 1000 marks?
# → How would you print all of them? Print all 1000 lines?!

# THE NEW WAY: Using Lists (MUCH better!)

marks = [50, 56, 89, 69, 67]
print("\nNEW WAY: One list for all")
print(marks)
print(f"Total students: {len(marks)}")


# ═══════════════════════════════════════════════════════════════
# PART 2: WHAT IS A LIST?
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PART 2: Understanding Lists")
print("=" * 60)

# A LIST is a container that holds MULTIPLE VALUES in ORDER
# Think of it like a backpack with numbered pockets:
#
# backpack = [50,  56,  89,  69,   67]
# indices:   [0,   1,   2,   3,    4]
#            ↑ Index starts at 0, NOT 1!

marks = [50, 56, 89, 69, 67]
print(f"\nMarks list: {marks}")
print(f"Data type: {type(marks)}")
print(f"Length (how many items): {len(marks)}")


# ═══════════════════════════════════════════════════════════════
# PART 3: ACCESSING ELEMENTS (Indexing)
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PART 3: Accessing Elements (Indexing)")
print("=" * 60)

marks = [50, 56, 89, 69, 67]
print(f"\nList: {marks}")
print(f"Index positions: [0, 1, 2, 3, 4]")

# FORWARD INDEXING (from the start):
print("\n--- FORWARD INDEXING ---")
print(f"marks[0] = {marks[0]}  (1st student)")
print(f"marks[1] = {marks[1]}  (2nd student)")
print(f"marks[2] = {marks[2]}  (3rd student)")
print(f"marks[4] = {marks[4]}  (last student)")

# NEGATIVE INDEXING (from the end):
print("\n--- NEGATIVE INDEXING ---")
print(f"marks[-1] = {marks[-1]}  (last student)")
print(f"marks[-2] = {marks[-2]}  (second last)")
print(f"marks[-3] = {marks[-3]}  (third last)")
# This is VERY useful when you don't know the list length!


# ═══════════════════════════════════════════════════════════════
# PART 4: MUTABILITY — Changing Values
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PART 4: Lists are MUTABLE (can be changed)")
print("=" * 60)

marks = [50, 56, 89, 69, 67]
print(f"\nOriginal list: {marks}")

# Student at index 2 had incorrect marks, let's fix it
print("\n🔧 Fixing student 3's score (index 2)...")
marks[2] = 100
print(f"Updated list: {marks}")

# What if all marks are scaled up by 5 points for extra credit?
print("\n🎓 Adding 5 bonus points to all students...")
marks[0] = marks[0] + 5
marks[1] = marks[1] + 5
marks[2] = marks[2] + 5
marks[3] = marks[3] + 5
marks[4] = marks[4] + 5
print(f"After bonus: {marks}")


# ═══════════════════════════════════════════════════════════════
# PART 5: LISTS CAN HOLD DIFFERENT DATA TYPES
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PART 5: Mixed Data Types in Lists")
print("=" * 60)

# A list doesn't have to contain only one type of data
mixed_list = [25, "Alice", 85.5, True, 10]
print(f"\nMixed list: {mixed_list}")
print("Elements:")
for i, item in enumerate(mixed_list):
    print(f"  Index {i}: {item} (type: {type(item).__name__})")

# REAL-WORLD EXAMPLE: Student Record
student_record = ["Devansh", 19, 89.5, True]  # name, age, marks, active
print(f"\nStudent record: {student_record}")
print(f"Name: {student_record[0]}")
print(f"Age: {student_record[1]}")
print(f"Marks: {student_record[2]}")


# ═══════════════════════════════════════════════════════════════
# PART 6: LIST SLICING — Getting Sub-Lists
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PART 6: Slicing Lists")
print("=" * 60)

marks = [50, 56, 89, 69, 67]
print(f"\nOriginal list: {marks}")
print("Indices:       [0,  1,  2,  3,  4]")

# Slicing: list[start : end]
# NOTE: end is EXCLUSIVE (not included)

print("\n--- BASIC SLICING ---")
print(f"marks[0:3]  = {marks[0:3]}  (from index 0 to 2, not 3)")
print(f"marks[1:4]  = {marks[1:4]}  (from index 1 to 3, not 4)")
print(f"marks[2:5]  = {marks[2:5]}  (from index 2 to 4)")

print("\n--- SHORTHAND SLICING ---")
print(f"marks[:3]   = {marks[:3]}    (from start to index 2)")
print(f"marks[2:]   = {marks[2:]}    (from index 2 to end)")
print(f"marks[:]    = {marks[:]}     (entire list copy)")

print("\n--- NEGATIVE SLICING ---")
print(f"marks[-3:]  = {marks[-3:]}   (last 3 elements)")
print(f"marks[:-2]  = {marks[:-2]}   (all except last 2)")
print(f"marks[-4:-1]= {marks[-4:-1]} (4th last to 2nd last)")

print("\n--- SLICING WITH STEP ---")
print(f"marks[::2]  = {marks[::2]}   (every 2nd element)")
print(f"marks[::-1] = {marks[::-1]}  (REVERSE the list!)")


# ═══════════════════════════════════════════════════════════════
# PART 7: LISTS ARE ORDERED
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PART 7: Lists Maintain Order")
print("=" * 60)

# Lists remember the order you add items
scores = [89, 45, 92, 67, 88]
print(f"\nScores in order: {scores}")
print("Position matters!")
print(f"  Highest score isn't always first: {scores[0]}")
print(f"  Lowest score: {min(scores)}")
print(f"  Highest score: {max(scores)}")


# ═══════════════════════════════════════════════════════════════
# PART 8: EMPTY LISTS & CREATING LISTS
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("PART 8: Creating Lists")
print("=" * 60)

# Empty list (start with nothing, add later)
empty_list = []
print(f"\nEmpty list: {empty_list}")
print(f"Length: {len(empty_list)}")

# List with initial values
numbers = [10, 20, 30, 40]
print(f"\nNumbers: {numbers}")

# List with repeated values
zeros = [0] * 5
print(f"Five zeros: {zeros}")

# List from range
range_list = list(range(1, 6))
print(f"Numbers 1-5: {range_list}")


# ═══════════════════════════════════════════════════════════════
# PART 9: KEY CONCEPTS SUMMARY
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
✓ Lists store multiple values in ONE variable
✓ Elements are accessed using INDEXING (start at 0)
✓ Use NEGATIVE indexing to access from the end (-1 = last item)
✓ Lists are MUTABLE (can change values)
✓ Use SLICING to get sub-lists [start:end]
✓ Lists maintain ORDER
✓ Lists can hold DIFFERENT data types

NEXT: You'll learn about LIST METHODS and LOOPS!
""")

# ═══════════════════════════════════════════════════════════════


# Dev's notes


cars = ["Verna","Porsche","Ciaz","Roll Royce","Massserati"]
print(cars)

print(len(cars))