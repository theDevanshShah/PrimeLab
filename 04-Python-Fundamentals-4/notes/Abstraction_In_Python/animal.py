"""Abstract classes and methods in Python."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract parent class that defines the Animal interface."""

    @abstractmethod
    def make_sound(self):
        """Every concrete animal must implement its own sound."""
        pass

    def describe(self):
        """A normal method can be shared by all child classes."""
        return "This is an animal"


# Animal is incomplete because make_sound() has no implementation here.
# This would raise TypeError:
# animal = Animal()


class Lion(Animal):
    """Concrete class that fulfills Animal's required contract."""

    def make_sound(self):
        return "Roar"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def make_sound(self):
        return "Woof"