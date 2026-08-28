"""
===============================================================================
                          POLYMORPHISM IN PYTHON
===============================================================================

Polymorphism means "many forms". The same method call can produce different
behavior depending on the object receiving the call.

This lesson covers:
    1. Method overriding
    2. Runtime polymorphism
    3. Using super() with an overridden method
    4. Duck typing
===============================================================================
"""


# =============================================================================
# 1. METHOD OVERRIDING
# =============================================================================

class Animal:
    def make_sound(self):
        return "Some animal sound"


class Dog(Animal):
    def make_sound(self):
        # Dog replaces, or overrides, the parent implementation.
        return "Bark"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


dog = Dog()
cat = Cat()

print("Dog:", dog.make_sound())
print("Cat:", cat.make_sound())
print("Animal:", Animal().make_sound())

# The method name is the same, but the result depends on the object's class.


# =============================================================================
# 2. RUNTIME POLYMORPHISM
# =============================================================================

# This function does not need separate code for Dog and Cat. It only expects
# an object that provides make_sound().
def announce_sound(animal):
    print(f"{animal.__class__.__name__} says {animal.make_sound()}")


print("\nRuntime polymorphism:")
for animal in (dog, cat, Animal()):
    announce_sound(animal)


# =============================================================================
# 3. super() WITH METHOD OVERRIDING
# =============================================================================

class Service:
    def start(self):
        return "Service has started"


class EmailService(Service):
    def start(self):
        parent_message = super().start()
        return f"{parent_message}; email service is ready"


email_service = EmailService()
print("\nUsing super():", email_service.start())

# super() lets a child reuse the parent's behavior before adding its own.


# =============================================================================
# 4. DUCK TYPING
# =============================================================================

# Duck typing means Python focuses on what an object can do, not what class it
# belongs to. The informal rule is: "If it walks like a duck and quacks like a
# duck, treat it like a duck."

class Person:
    def speak(self):
        return "Hello"


class Robot:
    def speak(self):
        return "Beep"


def make_it_speak(speaker):
    # No inheritance is required. The object only needs a speak() method.
    print(speaker.speak())


print("\nDuck typing:")
make_it_speak(Person())
make_it_speak(Robot())

# Person and Robot are unrelated classes, but both can be used by the same
# function because both provide the behavior that function needs.


# =============================================================================
# 5. DUCK TYPING WITH BUILT-IN OBJECTS
# =============================================================================

class Book:
    def read(self):
        return "Reading a book"


class Website:
    def read(self):
        return "Reading a website"


def read_content(content):
    print(content.read())


print("\nShared behavior without shared inheritance:")
read_content(Book())
read_content(Website())


# =============================================================================
# 6. OVERRIDING VS DUCK TYPING
# =============================================================================

print("\n--- Overriding vs Duck Typing ---")
print("Overriding: child classes replace a method inherited from a parent")
print("Polymorphism: one interface supports many different behaviors")
print("Duck typing: an object's behavior matters more than its class")
print("Inheritance is useful, but duck typing does not require inheritance")


# =============================================================================
# 7. QUICK SUMMARY
# =============================================================================

print("\n--- Quick Summary ---")
print("Same method call, different object, different behavior")
print("Overridden methods are selected at runtime")
print("super() reuses parent behavior")
print("Duck typing uses an object's available methods")
print("Good polymorphic code depends on behavior, not unnecessary class checks")
