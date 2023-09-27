# 1. Polymorphism mean to have many forms, It is the ability of one function to display multiple functionalities all together.
#  1.1 It basically creates a structure that can use many forms of objects.
# Here is an example of applying OOP Concepts:

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age,sound):
        self.name = name
        self.sound = sound
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def set_age(self,age):
        if age<10:
            raise ValueError("it is not allowed in this age")
        return age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.__age} years old.")

    @abstractmethod
    def make_sound():
        pass


class Cat(Animal):
    def make_sound(self):
        print(self.sound)


class Cow(Animal):
    def make_sound(self):
        print(self.sound)

def main():
    cat1 = Cat("Kitty", 11,"Meow")
    cow1 = Cow("Fluffy", 12,"Moo")

    for animal in (cat1, cow1):
        animal.make_sound()
        animal.info()
        animal.make_sound()

if __name__ == '__main__':
    main()