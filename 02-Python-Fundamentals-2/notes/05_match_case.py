# Match Case in Python (Python 3.10+)
# Similar to switch-case in other languages

# --- Basic match-case ---
day = input("Enter day number (1-7): ")

match day:
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case "4":
        print("Thursday")
    case "5":
        print("Friday")
    case "6":
        print("Saturday")
    case "7":
        print("Sunday")
    case _:
        print("Invalid day!")  # _ is the default/wildcard case

# --- match-case with HTTP status codes ---
status = int(input("Enter HTTP status code: "))

match status:
    case 200:
        print("OK - Success")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case 301 | 302:  # multiple values with |
        print("Redirect")
    case _:
        print("Unknown status code")

# --- When to use match-case vs if-elif ---
# match-case: when comparing ONE variable against MANY fixed values
# if-elif: when checking ranges or complex conditions
