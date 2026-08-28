"""
===============================================================================
                         ABSTRACTION EXAMPLES
===============================================================================

The user of a class only needs to know what a method does, not every detail of
how it works. An abstract class makes this design clear by defining a contract
that its child classes must follow.
===============================================================================
"""

from animal import Animal, Cat, Dog, Lion


# =============================================================================
# 1. CONCRETE OBJECTS
# =============================================================================

simba = Lion()
tom = Cat()
buddy = Dog()

print("Lion sound:", simba.make_sound())
print("Cat sound:", tom.make_sound())
print("Dog sound:", buddy.make_sound())
print("Shared method:", simba.describe())


# =============================================================================
# 2. ABSTRACTION AND POLYMORPHISM
# =============================================================================

# This function does not need to know whether it receives a Lion, Cat, or Dog.
# It only relies on the Animal contract: every Animal has make_sound().
def announce_sound(animal):
    print(f"{animal.__class__.__name__} says {animal.make_sound()}")


print("\nAnimal sounds:")
for animal in (simba, tom, buddy):
    announce_sound(animal)


# =============================================================================
# 3. WHY THE ABSTRACT CLASS CANNOT BE CREATED
# =============================================================================

try:
    Animal()
except TypeError as error:
    print("\nCannot create Animal directly:", error)

# Animal is only a design/template class. A subclass must implement every
# abstract method before Python allows that subclass to be instantiated.


# =============================================================================
# 4. WHAT HAPPENS WHEN A METHOD IS NOT IMPLEMENTED?
# =============================================================================

class Bird(Animal):
    pass


try:
    Bird()
except TypeError as error:
    print("Bird is still abstract:", error)


# =============================================================================
# 5. QUICK SUMMARY
# =============================================================================

print("\n--- Quick Summary ---")
print("Abstraction: expose the essential behavior and hide details")
print("ABC: base class for an abstract class")
print("@abstractmethod: required method for child classes")
print("Concrete class: implements all abstract methods")
print("Polymorphism: same method call, different child behavior")
