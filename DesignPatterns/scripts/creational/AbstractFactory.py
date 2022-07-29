# Reference: https://github.com/faif/python-patterns/blob/master/patterns/creational/abstract_factory.py

import random
from typing import Type


# AbsrtactProduct
class Pet:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


# ConcreteProduct
class Dog(Pet):
    def speak(self) -> None:
        print("woof")

    def __str__(self) -> str:
        return f"Dog<{self.name}>"


# ConcreteProduct
class Cat(Pet):
    def speak(self) -> None:
        print("meow")

    def __str__(self) -> str:
        return f"Cat<{self.name}>"


# ConcreteFactory
class PetShop:
    """A pet shop"""
    def __init__(self, animal_factory: Type[Pet]) -> None:
        """pet_factory is our abstract factory.  We can set it at will."""
        self.pet_factory = animal_factory

    def buy_pet(self, name: str) -> Pet:
        """Creates and shows a pet using the abstract factory"""
        pet = self.pet_factory(name)
        print(f"Here is your lovely {pet}")
        return pet


# Factory Method
def random_animal(name: str) -> Pet:
    """Let's be dynamic!"""
    return random.choice([Dog, Cat])(name)


if __name__ == "__main__":
    catShop = PetShop(Cat)  # 只能购买"猫"的宠物店
    cat = catShop.buy_pet("Kitty")
    petShop = PetShop(random_animal)
    for name in ["Anddy", "DouDou", "Mua"]:
        pet = petShop.buy_pet(name)
        pet.speak()
