from dataclasses import dataclass, field, InitVar
from typing import ClassVar
import hashlib

@dataclass(order=True)
class Point:
    x: int
    y: int

# __init__
# __repr__
# __eq__
# Order is set to False as Default

p1 = Point(1,2)
p2 = Point(2,1)
print(p1,p2)
print(p1==p2)

'''
In Python, if a class constructor uses a mutable object like a list ([]) as a default argument,
that default value is not recreated each time the class is instantiated. Instead, it is evaluated 
once at function definition time and reused across all instances. Because of this, the default list 
is shared by reference, not copied. As a result, if one instance appends to the list, the change is
visible in all other instances that rely on the default value. This behavior can lead to unintended
shared state and bugs unless handled properly.
'''

@dataclass
class InventoryItem:
    name:str
    unit_price: float
    quantity_on_hand: int = 0
    size: list[str] = field(default_factory=list)
    class_var: ClassVar[int] = 100

'''
Context:
An instance field is a variable that is stored on each object, and each object has its own copy.

If you create 10 objects -> there are 10 separate values.

ClassVar prevents a class-level attribute from being treated as an instance field by a dataclass

ClassVar prevents a class-level attribute from being treated as an instance field by a dataclass. You need a value to build the object, but you don’t want to store it
'''


#Inheritance

class Rectangle:
    def __init__(self, height, width):
        self.heigh  = height
        self.width  = width

@dataclass
class Square(Rectangle):
    side: float

    def __post_init__(self):
        super().__init__(self.side, self.side)


#Inheritance of two dataclass

@dataclass 
class Triangle:
    side1: int
    side2: int
    side3: int

@dataclass
class ColoredTriangle(Triangle):
    color: str

tri = ColoredTriangle(2,3,4,"blue")
print(tri)

@dataclass
class User:
    username: str
    raw_password: InitVar[str]
    password_hash: str = field(init=False)

    def __post_init__(self, raw_password):
        self.password_hash = hashlib.sha256(
            raw_password.encode()
        ).hexdigest


user1 = User("Jhonathan1234", "IloveKirby")
print(user1)

'''
In Python dataclasses, field() should be used only when special control over a field’s 
behavior is needed, not for every default value. It is appropriate to use field() when 
the default value is mutable (such as a list, dict, or set) and must be created per instance
 using default_factory, when a field should not appear in the generated __init__ method (init=False) 
 because it is derived internally, or when customizing behavior such as excluding a field from repr, 
 comparisons, or hashing. It should not be used for simple immutable defaults like integers, strings, 
 or booleans, since these do not cause shared-state issues and work correctly with normal assignment. 
 In short, field() exists to control dataclass mechanics, not as a replacement for ordinary default values.
'''