class Animal:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def speak(self):
        return f"I am {self.name}"

class Dog(Animal):
    def move(self):
        return f"{self.name} is running"
    
    def speak(self):
        return super().speak() + " and I say Woof!"

class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming"
    
    def speak(self):
        return super().speak() + " and I say Blub blub!"

class Bird(Animal):
    def move(self):
        return f"{self.name} is flying"
    
    def speak(self):
        return super().speak() + " and I say Tweet!"

class Snake(Animal):
    def move(self):
        return f"{self.name} is slithering"
    
    def speak(self):
        return super().speak() + " and I say Hiss!"

class Pegasus(Animal):
    def move(self):
        return f"{self.name} is galloping and flying"
    
    def speak(self):
        return super().speak() + " and I say Neigh!"

def animal_showcase(animals):
    print("Animal Movement Showcase")
    print("-----------------------")
    for animal in animals:
        print(animal.speak())
        print(animal.move())
        print()

# Create some animals
animals = [
    Dog("Rex"),
    Fish("Nemo"),
    Bird("Tweety"),
    Snake("Viper"),
    Pegasus("Skyrunner")
]

# Demonstrate polymorphism
animal_showcase(animals)