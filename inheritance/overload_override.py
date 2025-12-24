from typing import overload, override
from abc import ABC, abstractmethod


# -------------------------------------------------
# PART 1: @overload
# -------------------------------------------------

@overload
def parse(value: int) -> str: ...
@overload
def parse(value: str) -> int: ...

def parse(value):
    """
    Same function name.
    Different behavior based on input type.
    """
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return int(value)
    raise TypeError("Unsupported type")


# Usage (type checkers understand this)
result_str = parse(123)     # inferred as str
result_int = parse("456")   # inferred as int


# -------------------------------------------------
# PART 2: ABC + @override
# -------------------------------------------------

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass


class Dog(Animal):
    @override
    def speak(self) -> str:
        return "woof"


class Cat(Animal):
    @override
    def speak(self) -> str:
        return "meow"


# -------------------------------------------------
# PART 3: Runtime demo
# -------------------------------------------------

def main() -> None:
    print("parse(123) ->", parse(123))
    print('parse("456") ->', parse("456"))

    animals: list[Animal] = [Dog(), Cat()]
    for a in animals:
        print(a.speak())


if __name__ == "__main__":
    main()
