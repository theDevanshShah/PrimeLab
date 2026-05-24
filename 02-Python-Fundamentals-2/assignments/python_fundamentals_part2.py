# ============================================================
#  ASSIGNMENT — Python Fundamentals Part 2
#  Topics: Conditionals, Nesting, Match-Case, While/For Loops,
#          Break/Continue, range(), Functions, Lambda, Factorial
# ============================================================
#  Instructions:
#  - Write your solution below each question
#  - Run the file to test your answers
#  - Try solving WITHOUT looking at the notes first!
# ============================================================


# ============================================================
#  SECTION 1: CONDITIONALS (if / elif / else)
# ============================================================

# Q1. Take a number as input. Print "Positive", "Negative", or "Zero".
'''

number = int(input("Choose any number : "))
try:
    if(number > 0):
        print("Positive")
    elif(number < 0):
        print("Negative")
    else:
        print("It's a ZERO")
except ValueError:
    print("Ooops! Invalid Entry")
'''
    
# Q2. Take 3 numbers as input. Print the largest one.
#     (Use if-elif-else, NOT max() function)

'''
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

if(num1 > num2 and num1 > num3):
    print(num1)
elif(num2 > num1 and num2 > num3):
    print(num2)
else:
    print(num3)
'''

# Q3. Take a character as input. Check if it's a vowel or consonant.
#     Handle both uppercase and lowercase.
'''
character = input("Enter any character : ")

if character in "AEIOUaeiou":
    print("VOWEL")
else:
    (print("Consonant"))
'''

# Q4. Traffic Light: Take a color as input (red/yellow/green).
#     red → "STOP", yellow → "SLOW DOWN", green → "GO"
#     Anything else → "Invalid color"

'''
lightColor = input("Enter the color : ").lower()
if(lightColor == "RED"):
    print("STOP")
elif(lightColor == "YELLOW"):
    print("SLOW DOWN")
elif(lightColor == "GREEN"):
    print("GO")
else:
    print("Invalid Entry")

lightColorr = input("Enter the color : ").lower()

if lightColorr == "red":
      print("STOP")
elif lightColorr == "yellow":
      print("SLOW DOWN")
elif lightColorr == "green":
      print("GO")
else:
      print("Invalid Entry")
      
'''
      
# Q5. Ternary challenge: Take age as input.
#     In ONE line, print "Can Vote" if age >= 18, else "Cannot Vote".

#print("Can Vote" if int(input("Enter age: ")) >= 18 else "Cannot Vote") 

# ============================================================
#  SECTION 2: NESTING
# ============================================================

# Q6. Age Category — Take age as input. Print:
#     - If age < 18 → "Minor"
#       - If age < 5 → "Toddler"
#       - Else → "Kid/Teen"
#     - If age >= 18 → "Adult"
#       - If age >= 60 → "Senior Citizen"
#       - Else → "Working Age"
'''
age = int(input("Please enter valid age : "))

if(age < 18):
    print("Minor")
    if(age < 5):
        print("Toddler")
    else:
        print("Kid/Teen")
elif(age >= 18):
    print("Adult")
    if(age >= 60):
        print("Senior Citizen")
    else:
        print("Working Age")
'''

# Q7. Number Analyzer — Take a number as input.
#     First check: positive, negative, or zero.
#     If positive → is it even or odd?
#     If negative → is it even or odd?
#     If zero → "Zero is neither positive nor negative"
'''
number = int(input("Please Enter A Number : "))

if(number < 0):
    print("It's Negative and ... ")
    if(number % 2 == 0):
        print("It's Even")
    else:
        print("It's Odd")
elif(number > 0):
    print("It's Positive and ...")
    if(number % 2 == 0):
        print("It's Even")
    else:
        print("It's Odd")
elif(number == 0):
    print("Zero is neither positive nor negative")
else:
    print("Enter Valid Number")
'''

# Q8. Login System — Take username and password as input.
#     - If username is "dev" →
#       - If password is "python123" → "Login Successful!"
#       - Else → "Wrong Password!"
#     - Else → "User Not Found!"
'''
userName = input("Please Enter Valid UserName : ")
password = input("Please Enter Valid Password : ")

if(userName == "dev"):
    if(password == "python123"):
        print("Login SuccessFul!")
    else:
        print("Wrong Password!")
else:
    print("Wrong UserName")
'''

# Q9. Marks + Attendance — Take marks and attendance (int) as input.
#     - If attendance >= 75 →
#       - marks >= 90 → "Grade A"
#       - marks >= 60 → "Grade B"
#       - marks < 60 → "Fail"
#     - If attendance < 75 → "Detained - Low Attendance"
#       (don't even check marks)
'''
marks = int(input("Please Enter Valid Marks : "))
attendance = int(input("Please Enter Valid Attendance : "))

if(attendance >= 75):
    if(marks >= 90):
        print("Grade A")
    elif(marks >= 60):
        print("Grade B")
    else:
        print("Fail")
else:
    print("Detained -> Low Attendance")
'''

# Q10. Triangle Checker — Take 3 sides (a, b, c) as input.
#      - First: are all sides positive? If not → "Invalid sides"
#      - If valid → check triangle inequality (a+b>c, b+c>a, a+c>b)
#        - If yes → check type:
#          - All equal → "Equilateral"
#          - Two equal → "Isosceles"
#          - None equal → "Scalene"
#        - If no → "Not a triangle"
'''
A = int(input("Please Enter Side A : "))
B = int(input("Please Enter Side B : "))
C = int(input("Please Enter Side C : "))

if(A > 0  and B > 0  and C > 0):
    if((A + B > C) and (B + C > A) and (A + C > B)):
        print("IT'S A VALID TRIANGLE")
        if(A == B == C):
            print("Equilateral")
        elif(A == B or A == C or B == C):
            print("Isosceles")
        elif(A != B and B != C and C != A):
            print("Scalene")
    else:
        print("Not a triangle")
else:
    print("Invalid Sides")
'''
  
# ============================================================
#  SECTION 3: MATCH-CASE
# ============================================================

# Q11. Take a day number (1-7) as input. Print the day name.
#      1 → Monday, 2 → Tuesday ... 7 → Sunday
#      Anything else → "Invalid day"
#      (Use match-case, NOT if-elif)
'''
dayNumber = int(input("Please Enter A Valid Number Between 1-7 : "))

match dayNumber:
    case 1 : print("Monday")
    case 2 : print("Tuesday")
    case 3 : print("Wednesday")
    case 4 : print("Thursday")
    case 5 : print("Friday")
    case 6 : print("Saturday")
    case 7 : print("Sunday")
    case _ : print("Invalid Day") 
'''
    
# Q12. Simple Calculator using match-case:
#      Take num1, operator (+,-,*,/), and num2 as input.
#      Match the operator and print the result.
#      Handle division by zero!
'''
num1 = int(input("Please Enter Valid Number 1 : "))
num2 = int(input("Please Enter Valid Number 2 : "))
operator = input("Please Enter Valid Operator From -> + , - , / , * : ")

match operator:
    case "+": print(f"{num1} + {num2} = {num1 + num2}")
    case "-": print(f"{num1} - {num2} = {num1 - num2}")
    case "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Cannot divide by zero!")
    case "*": print(f"{num1} * {num2} = {num1 * num2}")
    case _: print("Invalid Operator")
'''

# ============================================================
#  SECTION 4: WHILE LOOP
# ============================================================
#Practise
'''
#Increament
counter = 1

while counter <= 5:
    print("Hi")
    counter = counter
    + 1
'''
#Decreament
'''
counter = 5

while counter >= 1:
    print(counter)
    counter = counter - 1
'''

# Q13. Print numbers from 1 to 20 using a while loop.
'''
number = 1

while number <=20:
    print(number)
    number = number + 1
'''
# Q14. Print all EVEN numbers from 2 to 50 using while.
'''
number = 2

while number <=50:
    print(number)
    number = number + 2
'''
            
# Q15. Take a number as input. Count how many digits it has.
#      (Use while loop with //= 10, NOT len(str(n)))
'''
inputNumber = int(input("Please Enter A Valid Number : "))
print("Your Original Number Is : ", inputNumber)
count = 0
while inputNumber > 0:
    inputNumber = inputNumber // 10
    count = count + 1
    
print("There Are ", count , " Digits In Your Number")
'''

# Q16. Take a number as input. Print the REVERSE of the number.
#      Example: 12345 → 54321
#      (Use while loop with % and //, NOT string slicing)

# reversed = 0
# inputNumber = int(input("Please Enter A Valid Value : "))

# while inputNumber > 0:
#     digit = inputNumber % 10
#     reversed = reversed * 10 + digit
#     inputNumber = inputNumber // 10

# print(reversed)

# Q17. Take a number as input. Find the SUM of its digits.
#      Example: 9876 → 9+8+7+6 = 30

# sum = 0
# inputNumber = int(input("Please Enter a valid number : "))
# while inputNumber > 0:
#     digit = inputNumber % 10
#     sum = sum + digit
#     inputNumber = inputNumber // 10

# print(sum)

# Q18. Take a number as input. Check if it's a PALINDROME.
#      Example: 121 → Palindrome, 123 → Not Palindrome
#      (Reverse it using while loop, then compare)


# reversed = 0
# inputNumber = int(input("Please Enter A Valid Value : "))
# originalNumber = inputNumber

# while inputNumber > 0:
#     digit = inputNumber % 10
#     reversed = reversed * 10 + digit
#     inputNumber = inputNumber // 10

# if(reversed == originalNumber):
#     print("PALINDROME")
# else:
#     print("No Palindrome")

# ============================================================
#  SECTION 5: FOR LOOP & range()
# ============================================================

# Practise

# stringWord = "HELLOW"

# for varo in stringWord:
#     print(varo)
# string = "Hellow"
# if 'o' in string:
#     print("Yess")
# Q19. Print numbers from 1 to 10 using for loop and range().

# for i in range(1,11):
#     print(i)

# for i in range(10):
#     print(i+1)

# # Q20. Print all numbers from 50 to 1 (countdown) using range().

# for j in range(51,1,-1):
#     print(j-1)

# # # Q21. Print all multiples of 7 between 1 and 100.

# # for k in range(1,101):
# #     if(k % 7 == 0):
# #         print(k)

# # Q22. Take a string as input. Count the number of vowels in it.

# string = input("Enter a string : ")
# count = 0

# for char in string:
#     if(char in "AEIOUaeiou"):
#         count = count + 1

# print(count)

# Q23. Print this pattern using nested for loops:
#      *
#      * *
#      * * *
#      * * * *
#      * * * * *

# for i in range(1,6):
#     for j in range(1, i + 1):
#         print("*",end = " ")
#     print()
    

# Q24. Print this pattern:
#      * * * * *
#      * * * *
#      * * *
#      * *
#      *
# for i in range(7,1,-1):
#     for j in range(1, i - 1):
#         print("*",end = " ")
#     print()

# Q25. Print multiplication table of a number from 1 to 10.
#      Format: 5 x 1 = 5, 5 x 2 = 10, etc.

# n = 5

# for digit in range(1,11):
#     print(n, " x ", digit ," = ", digit * n)

# ============================================================
#  SECTION 6: BREAK & CONTINUE
# ============================================================

# Q26. Print numbers from 1 to 20, but STOP when you hit 13.
#      (Use break)


# Q27. Print numbers from 1 to 20, but SKIP multiples of 3.
#      (Use continue)


# Q28. Take numbers as input in a loop. Stop when user enters 0.
#      Print the sum of all numbers entered.
#      (Use while True with break)


# Q29. Find the FIRST number between 100 and 200 that is
#      divisible by both 3 and 7. Print it and stop.


# ============================================================
#  SECTION 7: FUNCTIONS
# ============================================================

# Q30. Write a function greet(name) that prints "Hello, [name]!".
#      Call it 3 times with different names.


# Q31. Write a function add(a, b) that RETURNS the sum.
#      Print the result of add(10, 20).


# Q32. Write a function is_even(n) that returns True if even, False if odd.
#      Test it with 4 and 7.


# Q33. Write a function max_of_three(a, b, c) that returns the largest.
#      Don't use the built-in max() function.


# Q34. Write a function power(base, exp=2) with DEFAULT parameter.
#      power(5) should return 25, power(5, 3) should return 125.


# Q35. Write a function that takes a number and returns TWO values:
#      the square and the cube. Use tuple unpacking to print both.


# Q36. Write a function is_prime(n) that returns True if prime.
#      Test with: 2, 7, 10, 13, 1, 0


# Q37. Write a function count_vowels(text) that returns the
#      number of vowels in a string. Test with "Devansh Shah".


# ============================================================
#  SECTION 8: LAMBDA FUNCTIONS
# ============================================================

# Q38. Write a lambda function that doubles a number.
#      Test: double(5) → 10


# Q39. Write a lambda function that checks if a number is positive.
#      Test: is_positive(5) → True, is_positive(-3) → False


# Q40. Given this list: [3, 1, 4, 1, 5, 9, 2, 6]
#      Use filter() with lambda to get only numbers > 4.


# Q41. Given this list: [1, 2, 3, 4, 5]
#      Use map() with lambda to get the cube of each number.


# Q42. Given: students = [("Dev", 85), ("Alice", 92), ("Bob", 78)]
#      Sort by marks (second element) using sort() with lambda.


# ============================================================
#  SECTION 9: RECURSION & FACTORIAL
# ============================================================

# Q43. Write a function factorial(n) using a FOR LOOP.
#      Test: factorial(5) → 120, factorial(0) → 1


# Q44. Write a function factorial_recursive(n) using RECURSION.
#      Test with same values.


# Q45. Write a recursive function sum_n(n) that returns
#      the sum of first n natural numbers.
#      sum_n(5) → 15 (1+2+3+4+5)


# Q46. Write a recursive function countdown(n) that prints
#      n, n-1, n-2, ..., 1, "Go!"


# ============================================================
#  SECTION 10: MIXED PRACTICE (COMBINE EVERYTHING!)
# ============================================================

# Q47. Write a function that takes a number and returns
#      whether it's a palindrome AND whether it's even/odd.
#      Example: check(121) → "121 is a Palindrome and Odd"


# Q48. FizzBuzz — Print numbers 1 to 50:
#      - Divisible by 3 → "Fizz"
#      - Divisible by 5 → "Buzz"
#      - Divisible by both → "FizzBuzz"
#      - Otherwise → the number itself


# Q49. Write a function that takes a list of numbers and returns:
#      - count of positives
#      - count of negatives
#      - count of zeros
#      Test with: [1, -2, 0, 3, -4, 0, 5, -6, 0]


# Q50. ATM Machine Simulator:
#      - Start with balance = 10000
#      - Loop: show menu (1. Check Balance, 2. Deposit,
#        3. Withdraw, 4. Exit)
#      - Take choice as input using match-case
#      - Deposit: add amount to balance
#      - Withdraw: check if sufficient balance first
#      - Exit: break the loop
#      - Invalid choice: print "Invalid option"
#      Use: while True, match-case, functions, if-else


# ============================================================
#  ALL THE BEST, DEV! 🔥
#  50 questions — conditionals se lekar ATM simulator tak.
#  Solve all, then show me!
# ============================================================
