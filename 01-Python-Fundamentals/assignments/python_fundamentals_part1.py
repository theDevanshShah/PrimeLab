# ============================================================
#  ASSIGNMENT — Python Fundamentals Part 1
#  Topics: Output, Variables, Data Types, Type Conversion,
#          Operators, Precedence, Input, Practice Problems
# ============================================================
#  Instructions:
#  - Write your solution below each question
#  - Run the file to test your answers
#  - Try solving WITHOUT looking at the notes first!
# ============================================================


# ============================================================
#  SECTION 1: OUTPUT & print()
# ============================================================

# Q1. Print your full name, age, and city — each on a separate line.
print("Full Name : Devansh Shah")
print("Age : 24")
print("City : Vadodara")


# Q2. Print this exact output using a SINGLE print statement:
#     Name: Dev | Age: 21 | City: Ahmedabad
print("Name: Dev | Age: 21 | City: Ahmedabad")


# Q3. What will be the output? Write your answer in a comment, then verify by running.
print(5 + 3)
print("5 + 3")
print("5" + "3")

# Outputs will be ,
# 8
# 5 + 3
# 53


# Q4. Print a box like this using print statements:
#     +----------+
#     |  PYTHON  |
#     +----------+
print("+----------+")
print("|  PYTHON  |")
print("+----------+")

# Q5. Print this using escape characters (\n and \t):
#     Language:	Python
#     Creator:	Guido van Rossum
#     Year:	1991
print("\tLanguage: Python \n\tCreator: Guido Van Rossum \n\tYear: 1991")

# ============================================================
#  SECTION 2: VARIABLES & NAMING RULES
# ============================================================

# Q6. Create 4 variables: your name (str), age (int), height (float),
#     and whether you're a student (bool). Print all of them.
name = "Dev"
age = 24
height = 5.8
isStudent = True
print("Hello Guys My Name Is " + name + " & I am ", age ," Years Old. My Height Is : ", height ," & Am I a Student ?", isStudent)


# Q7. Which of these variable names are INVALID? Fix the invalid ones.
#     Write your answers as comments.
#
#     my_name = "Dev"
#     2fast = "too fast"
#     _secret = 42
#     class = "AI"
#     my-age = 21
#     Name1 = "Shah"
#     for = 10
#     __init = True

'''
Invalid Ones : 
2Fast, class, Name1, for
'''
'''
Fixed Ones :
Too_Fast, we cant use Class & For because they're reserved keywords of the language, Name_One'''

# Q8. Swap two variables WITHOUT using a third variable.
#     Start with: a = "hello", b = "world"
#     After swap: a should be "world", b should be "hello"

a = "hello"
b = "world"
a == "hello", b == "world"
print("Before Swap : ")
print("a = " + a)
print("b = " + b)

#Swappig Logic
a == "world"
b == "hello"

print("After Swap : ")
print("a = " + a)
print("b = " + b)

# Q9. Swap two variables USING a third (temp) variable.
#     Start with: x = 100, y = 200
#     After swap: x should be 200, y should be 100
#     (Remember: save before you overwrite!)
x = 0
y = 0
x == 100, y == 200
print("Before Swap : ")
print("x = ", x)
print("y = ", y)

#Swappig Logic
z = 0
y == x
z == y
x == z

print("After Swap : ")
print("x = ", x)
print("y = ", y)

# Q10. What will be the output? Don't run it — think first, then verify.
#      a = 10
#      b = a
#      a = 20
#      print(a, b)
# it can be umm, 20 10

a = 10
b = a
a = 20
print(a,b)

# ============================================================
#  SECTION 3: DATA TYPES & type()
# ============================================================

# Q11. Predict the type of each value. Write your answers as comments,
#      then verify using type().
#
#      42
#      3.14
#      "3.14"
#      True
#      None
#      0
#      ""
#      0.0

# int
# float
# str
# Boolean
# none
# int
# str
# float

print(type(42))
print(type(3.14))
print(type("3.14"))
print(type(True))
print(type(None))
print(type(0))
print(type(""))
print(type(0.0))

# Q12. Create one variable of each type: int, float, str, bool, NoneType.
#      Print each variable along with its type using type().
a = 42
b = 3.14
c = "DEV"
d = False
e = None

print("Printing each variable along with its type using type().")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Q13. What is type(True + 10)? Why? Explain in a comment.
# it will be int. because True's value is 1 & 10 + 1 = 11. 11 is int
print(type(True + 10))

# Q14. What is the difference between these? Explain in comments.
#      a = 5
#      b = 5.0
#      c = "5"
'''
a is int
b is float
c is string
'''

# ============================================================
#  SECTION 4: TYPE CONVERSION & CASTING
# ============================================================

# Q15. Convert the string "99" to an integer and add 1 to it. Print the result.


# Q16. What will int(7.9) return? What about int(-7.9)?
#      Explain WHY in a comment (hint: it's not rounding).


# Q17. What will happen if you run: int("hello")?
#      Write your answer as a comment (don't crash your program!).


# Q18. Fix this code so it runs without error:
#      age = 21
#      print("I am " + age + " years old")


# Q19. What will these return? Predict first, then verify.
#      bool(0)
#      bool("")
#      bool("False")
#      bool(1)
#      bool(-5)
#      bool(None)
#      bool([])
#      bool("0")


# Q20. Convert the number 65 to its ASCII character using chr().
#      Convert the character 'Z' to its ASCII number using ord().


# ============================================================
#  SECTION 5: ARITHMETIC OPERATORS
# ============================================================

# Q21. Take two numbers a = 17 and b = 5. Print the result of:
#      addition, subtraction, multiplication, division,
#      floor division, modulus, and exponentiation.

a == 17
b == 5

print("a + b = ", a+b)
print("a - b = ", a-b)
print("a * b = ", a*b)
print("a / b = ", a/b)
#print("a  b = ", ab) idk floor division
#print("a  b = ", ab) idk modulus
print("a ** b = ", a**b)


# Q22. What is the difference between / and //?
#      Show with example: 17/5 vs 17//5 and -17//5. Explain in comments.
# 17/5 is simple division 17//5 is floor division

# Q23. Write a program to check if a number is even or odd using %.


# Q24. Given num = 98765, extract EACH digit using only // and %.
#      (No strings allowed!)
#      Expected output: 9 8 7 6 5 (each on separate line)


# Q25. What is 2 ** 10? What about 2 ** -3? Explain both in comments.


# ============================================================
#  SECTION 6: RELATIONAL (COMPARISON) OPERATORS
# ============================================================

# Q26. Predict True or False for each. Write answers as comments, then verify.
#      10 == 10.0
#      "hello" == "Hello"
#      1 == True
#      0 == False
#      None == False
#      None == 0


# Q27. Write a program: take marks as input. Print the grade:
#      90+ → A, 80-89 → B, 70-79 → C, 60-69 → D, below 60 → F


# Q28. Rewrite this using chained comparison (Python's special feature):
#      age = 25
#      if age >= 18 and age <= 60:
#          print("Working age")


# Q29. What will "apple" > "banana" return? Why?
#      What about "cat" > "car"? Explain in comments.


# ============================================================
#  SECTION 7: ASSIGNMENT OPERATORS
# ============================================================

# Q30. Start with x = 50. Perform these operations IN ORDER using
#      assignment operators (+=, -=, etc.) and print after each step:
#      - Add 30
#      - Subtract 15
#      - Multiply by 2
#      - Floor divide by 3
#      - Find remainder when divided by 7
#      - Raise to power 2


# Q31. What will x be after this? Think step by step.
#      x = 10
#      x += 5     # x = ?
#      x *= 2     # x = ?
#      x -= 10    # x = ?
#      x //= 3    # x = ?
#      x **= 2    # x = ?


# Q32. Start with message = "Python". Use += to build this string:
#      "Python is awesome!"


# ============================================================
#  SECTION 8: LOGICAL OPERATORS (and, or, not)
# ============================================================

# Q33. Predict the output. Write answers as comments, then verify.
#      print(True and True)
#      print(True and False)
#      print(False or True)
#      print(False or False)
#      print(not True)
#      print(not not True)


# Q34. What will these return? (Tricky! Think carefully)
#      print(5 > 3 and 10 < 20)
#      print(5 > 3 or 10 > 20)
#      print(not 5 > 3)
#      print(not False and True)
#      print(True or False and False)


# Q35. Write a program: take age and has_license as input.
#      Print "Can drive" only if age >= 18 AND has_license is True.
#      Print "Cannot drive" otherwise.


# Q36. Eligibility checker: A person can vote if:
#      - age >= 18 AND
#      - is_citizen is True AND
#      - is_registered is True
#      Take all 3 inputs and print "Eligible" or "Not Eligible".


# Q37. What are SHORT-CIRCUIT evaluations?
#      What will happen here and why? Explain in comments.
#      x = 0
#      result = x != 0 and 10 / x > 2


# ============================================================
#  SECTION 9: OPERATOR PRECEDENCE
# ============================================================

# Q38. What is the result of each? Solve on paper first, then verify.
#      2 + 3 * 4
#      (2 + 3) * 4
#      2 ** 3 ** 2
#      10 - 3 * 2 + 1
#      15 // 4 + 15 % 4
#      2 * 3 + 4 / 2 - 1


# Q39. Add parentheses to make this expression equal to 36:
#      2 + 4 * 8 - 2
#      (Write multiple ways if possible)


# Q40. True or False? Solve step by step in comments.
#      result = 5 > 3 and not 2 > 4 or 10 == 5


# ============================================================
#  SECTION 10: USER INPUT
# ============================================================

# Q41. Take the user's name and age as input.
#      Print: "Hello [name]! You will turn [age+1] next year."


# Q42. Take 3 numbers as input on a SINGLE line (space separated).
#      Print their sum.
#      Hint: use split() and map()


# Q43. Take temperature in Celsius as input.
#      Convert to Fahrenheit: F = (C × 9/5) + 32
#      Print the result.


# Q44. Take the radius of a circle as input.
#      Print its area (π × r²) and circumference (2 × π × r).
#      Use 3.14159 for π.


# ============================================================
#  SECTION 11: MIXED PRACTICE (COMBINE EVERYTHING!)
# ============================================================

# Q45. Take a 4-digit number as input. Print:
#      - Sum of all digits
#      - Reverse of the number
#      (Use only arithmetic operators, NO strings!)


# Q46. Take a number as input. Print whether it is:
#      - Positive or Negative or Zero
#      - Even or Odd
#      - Divisible by 5 or not


# Q47. Simple Interest Calculator:
#      Take principal (P), rate (R), and time (T) as input.
#      Calculate SI = (P × R × T) / 100
#      Print the Simple Interest and Total Amount (P + SI).


# Q48. BMI Calculator:
#      Take weight (kg) and height (m) as input.
#      BMI = weight / (height ** 2)
#      Print BMI and category:
#      BMI < 18.5 → Underweight
#      18.5 - 24.9 → Normal
#      25.0 - 29.9 → Overweight
#      30+ → Obese


# Q49. Electricity Bill Calculator:
#      Take units consumed as input.
#      First 100 units → Rs.5 per unit
#      Next 100 units → Rs.8 per unit
#      Above 200 units → Rs.10 per unit
#      Print total bill.


# Q50. BONUS — The Ultimate Test:
#      Without running, predict the FINAL value of x. Show each step.
#
#      x = 5
#      x += 3          # x = ? 8
#      x *= 2          # x = ? 16
#      x -= x // 3     # x = ?
#      x = x % 7       # x = ?
#      x **= 2         # x = ? 25
#      x = not (x > 50) # x = ?
#      print(x)
#
#      Write your step-by-step working as comments, then run to verify!


# ============================================================
#  ALL THE BEST, DEV! 🔥
#  Solve all 50, then let's review together.
# ============================================================
