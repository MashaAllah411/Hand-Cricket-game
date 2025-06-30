# method Overriding

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):  # Overrides Animal's speak
        return "Bark"

class Cat(Animal):
    def speak(self):  # Overrides Animal's speak
        return "Meow"

def Sounds(animal):
    print(animal.speak())

Sounds(Cat())  # Output: Meow
Sounds(Dog())  # Output: Bark

# Run-time polymorphism means that the method to be executed is determined during runtime, not at compile time. 
# This is typically achieved using method overriding in object-oriented programming.

class dog:
    def speak(self):
        return "Brak"
    
class cat:
    def speak(self):
        return "Meow"
    
def Sounds(animal):
    print(animal.speak())

Sounds(cat())