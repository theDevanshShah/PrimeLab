from animal import Animal

class Lion(Animal):
    def makeSound(self):
        print("Roar")
        
simba = Lion()
simba.makeSound()

class Cat(Animal):
    def makeSound(self):
        print("Meaw")
        
tom = Cat()
tom.makeSound()