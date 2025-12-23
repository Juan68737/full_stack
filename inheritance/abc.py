from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Abstract Base Class:
    - Cannot be instantiated
    - Enforces required methods + properties at runtime
    """

    max_speed: int  # abstract class attribute

    @abstractmethod
    def go(self) -> None:
        print("Vehicle starting...")

    @abstractmethod
    def stop(self) -> None:
        print("Vehicle stopping...")

    @property
    @abstractmethod
    def wheels(self) -> int:
        pass


class Bike(Vehicle):

    max_speed = 30

    def go(self) -> None:
        super().go()
        print("Bike Goes!")

    def stop(self) -> None:
        super().stop()
        print("Bike Stops!")

    @property
    def wheels(self) -> int:
        return 2


bike = Bike()
bike.go()
bike.stop()
print(bike.wheels)

print(isinstance(bike, Vehicle))
print(issubclass(Bike, Vehicle))
