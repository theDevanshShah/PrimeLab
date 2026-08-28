"""Sets in Python.

A set stores unique values. Sets are useful for membership tests and
set operations such as union and intersection.
"""

# A set removes duplicate values automatically.
numbers = {1, 2, 3, 4, 5, 5}
print("Unique numbers:", numbers)
print("Type:", type(numbers))

# Sets are unordered, so do not use indexes to access their values.
numbers.add(6)
print("After add():", numbers)

# {} creates an empty dictionary, not an empty set.
empty_dictionary = {}
print("Empty dictionary:", empty_dictionary)
print("Dictionary type:", type(empty_dictionary))

empty_set = set()
print("Empty set:", empty_set)
print("Set type:", type(empty_set))


# -----------------------------------------------------------------------------
# Adding, removing, and checking values
# -----------------------------------------------------------------------------

numbers.remove(5)
print("After remove():", numbers)

# discard() does not raise an error when the value is absent.
numbers.discard(100)
print("After discard() with a missing value:", numbers)

print("Is 3 present?", 3 in numbers)
print("Is 100 absent?", 100 not in numbers)

numbers.clear()
print("After clear():", numbers)


# -----------------------------------------------------------------------------
# Set operations
# -----------------------------------------------------------------------------

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet 1:", set1)
print("Set 2:", set2)
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Only in set 1:", set1.difference(set2))
print("Only in set 2:", set2.difference(set1))
print("Not shared by both:", set1.symmetric_difference(set2))

# The operators are shorter versions of the methods above.
print("\nUnion with |:", set1 | set2)
print("Intersection with &:", set1 & set2)
print("Difference with -:", set1 - set2)
print("Symmetric difference with ^:", set1 ^ set2)


# -----------------------------------------------------------------------------
# Subsets, supersets, and disjoint sets
# -----------------------------------------------------------------------------

small_set = {1, 2}
large_set = {1, 2, 3, 4}
other_set = {10, 20}

print("\nIs small_set a subset?", small_set.issubset(large_set))
print("Is large_set a superset?", large_set.issuperset(small_set))
print("Are the sets disjoint?", large_set.isdisjoint(other_set))