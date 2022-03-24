# ***** Classes

# ***** Class Attributes and Methods
class Dog:

    # Class Object Attribute
    # Same for any instance of a class

    species = "canine"

    def __init__(self, breed, name, age):

        # Attributes
        # Take in an argument and assign it to self.attribute_name
        self.breed = breed
        self.name = name
        self.age = age

    # Methods are functions inside a class
    def bark(self, food):
        print(f"Woof! My name is {self.name} and my favorite food is {food}.")


my_dog = Dog("Corgi", "Ein", 3)

print(type(my_dog))
print(my_dog.breed, my_dog.name, my_dog.age, my_dog.species)
my_dog.bark("beef")


class Circle:

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        # can use self.pi or Circle.pi but the latter makes it more obvious that it is a Class Object Attribute (not an attribute passed in as an argument)
        self.area = radius * radius * Circle.pi

    def get_circumference(self):
        return self.radius * Circle.pi * 2


my_circle = Circle(30)
print(my_circle.get_circumference())
print(my_circle.area)


# ****** Inheritance


class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("nom nom nom")


my_animal = Animal()

# This is a derived class because it is deriving features from the base class of Animal
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog")

    def bark(self):
        print("WOOF!")


my_dog = Dog()

# The Dog class inherited all the attributes and methods from the Animal class
my_dog.eat()

# This method was refactored in the Dog class
my_dog.who_am_i()

# This is a method that was created in the Dog class
my_dog.bark()


# ****** Polymorphism

# Different Object classes can share the same method name and the methods can be called from the same place as long as the different Objects have the same method name


class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


Warwick = Dog("Warwick")
Yuumi = Cat("Yuumi")

print(Warwick.speak())
print(Yuumi.speak())

# The speak method is being called in the for loop on two different Objects

for pet in [Warwick, Yuumi]:
    print(type(pet))
    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())


# The speak method is being called in the function on two different Objects
pet_speak(Warwick)
pet_speak(Yuumi)


# Abstract Classes and Inheritance
# Classes that only serve as a base class
# These classes are to be used by inheritance NOT instantiated themselves


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


# These two lines won't work properly because we don't expect Animal to be instantiated
# my_animal = Animal("fred")
# my_animal.speak()


class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"


class Cat(Animal):
    def speak(self):
        return self.name + " says weow!"


fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak())
print(isis.speak())


# ****** Magic/Dunder Methods


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # without the magic method __str__ printing the instance of Book only shows it's location in memory
    def __str__(self):
        return f"{self.title} by {self.author}"

    # __len__ allows for len to be used
    def __len__(self):
        return self.pages

    # __del__ allows you to execute code when the instance is deleted
    def __del__(self):
        print("A book object has been deleted")


b = Book("Mistborn", "Brandon Sanderson", 541)


print(b)
print(len(b))
del b
