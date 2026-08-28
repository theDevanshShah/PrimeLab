"""
===============================================================================
                    CLASSES AND OBJECTS IN PYTHON
===============================================================================

A class is a blueprint for creating objects.
An object is an instance of a class.

This lesson covers classes, objects, attributes, methods, self, __init__,
class attributes, instance attributes, class methods, and static methods.
===============================================================================
"""


# =============================================================================
# 1. CLASS, OBJECT, ATTRIBUTE, AND METHOD
# =============================================================================

class Student:
    """A blueprint for creating student objects."""

    subject = "Python"  # Class attribute shared by Student objects.

    def print_name(self):
        """Print the name stored in the current object."""
        print("The name of the student is", self.name)


student1 = Student()  # student1 is an object, or instance, of Student.
student1.name = "Dev"  # Instance attribute belonging to student1.

print("Student name:", student1.name)
print("Object type:", type(student1))
print("Class type:", type(Student))
student1.print_name()

# type(student1) shows the class that created the object.
# __main__ means this file is being run directly.
# type(Student) is type because classes are objects created by Python.


# =============================================================================
# 2. self AND INSTANCE METHODS
# =============================================================================

class Person:
    name = "Unknown"
    occupation = "Unknown"

    def introduce(self):
        print(f"{self.name} is a {self.occupation}")


person1 = Person()
person1.name = "Dev"
person1.occupation = "student"
person1.introduce()

person2 = Person()
person2.name = "Aarav"
person2.occupation = "developer"
person2.introduce()

# Python automatically sends the calling object as self.
# self.name means the name of the object calling the method.


# =============================================================================
# 3. THE __init__ METHOD (CONSTRUCTOR)
# =============================================================================

class Actor:
    def __init__(self, first_name, last_name):
        """Initialize each new Actor object with its own data."""
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


actor1 = Actor("Hritik", "Roshan")
print("Actor:", actor1.full_name())

# __init__ runs automatically when an object is created.
# self.first_name and self.last_name are instance attributes.


# =============================================================================
# 4. CLASS ATTRIBUTES AND INSTANCE ATTRIBUTES
# =============================================================================

class Car:
    wheels = 4  # Class attribute: normally shared by every car.

    def __init__(self, model, color):
        self.model = model  # Instance attribute: can differ per car.
        self.color = color

    def describe(self):
        print(f"{self.model} has {self.wheels} wheels and is {self.color}.")


audi = Car("A8", "BLACK")
bmw = Car("M3", "BLUE")
audi.describe()
bmw.describe()

# An instance can override a class attribute for itself.
audi.wheels = 5
print("Audi wheels:", audi.wheels)
print("BMW wheels:", bmw.wheels)
print("Car class wheels:", Car.wheels)


# =============================================================================
# 5. DEFAULT AND PARAMETERIZED CONSTRUCTORS
# =============================================================================

class Food:
    def __init__(self):
        print("A Food object was created")


dish = Food()


class Smartphone:
    operating_system = "iOS"  # Class attribute.

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def describe(self):
        print(
            f"This is an {self.operating_system} phone, "
            f"model {self.model}, in {self.color}."
        )


iphone1 = Smartphone(17, "Blue")
iphone2 = Smartphone(16, "Black")
iphone1.describe()
iphone2.describe()

# A constructor without extra arguments is often called a default constructor.
# A constructor accepting values is called a parameterized constructor.


# =============================================================================
# 6. THREE TYPES OF METHODS
# =============================================================================

class Coffee:
    coffee_beans = "Medium roasted"  # Class attribute.

    def __init__(self, ingredients, size):
        self.ingredients = ingredients
        self.size = size

    def order_details(self):
        """Instance method: receives self and uses object data."""
        return f"{self.size} coffee with {self.ingredients}"

    @classmethod
    def show_beans(cls):
        """Class method: receives cls and uses class data."""
        return f"Coffee beans: {cls.coffee_beans}"

    @staticmethod
    def calculate_price(price, discount):
        """Static method: needs neither self nor cls."""
        return price - discount


coffee1 = Coffee("Milk", "Venti")
print("\nOrder:", coffee1.order_details())
print(Coffee.show_beans())
print("Final price:", Coffee.calculate_price(100, 10))

# Instance method -> uses one object's data through self.
# Class method    -> uses class data through cls.
# Static method   -> a related utility that uses neither object nor class data.


# =============================================================================
# 7. QUICK SUMMARY
# =============================================================================

print("\n--- Quick Summary ---")
print("Class: blueprint for objects")
print("Object: instance of a class")
print("Attribute: data stored in a class or object")
print("Method: function defined inside a class")
print("self: the current object")
print("cls: the current class")
print("__init__: initializes a new object")