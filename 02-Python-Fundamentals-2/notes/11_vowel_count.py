# Vowel Count Program

# Count the number of vowels in a string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels in '{text}' = {count}")

# --- Bonus: Count each vowel separately ---
text = input("\nEnter another string: ")
text_lower = text.lower()

a_count = text_lower.count('a')
e_count = text_lower.count('e')
i_count = text_lower.count('i')
o_count = text_lower.count('o')
u_count = text_lower.count('u')

print(f"a: {a_count}, e: {e_count}, i: {i_count}, o: {o_count}, u: {u_count}")
print(f"Total vowels: {a_count + e_count + i_count + o_count + u_count}")
