from collections import namedtuple
from typing import NamedTuple


#namedTuple
Point = namedtuple("Point", ["x", "y"])

p1 = Point(3,4)
print(isinstance(p1, tuple)) # -> True

print(p1.x) # -> 3
print(p1.y) # -> 4
print(p1[0]) # -> 3
print(p1[1]) # -> 4

#p.x = 10   # AttributeError

'''
Why use namedtuple instead of a normal tuple?

p = (3, 4)
p[0]  # what is this again?

p = Point(3, 4)
p.x   # obvious meaning

Its still a tuple while also behaving like a map at the same time 

'''

#Under the hood the namedTuple is making something like this

class Point(tuple):
    __slots__ = ()
    _fields = ("x", "y")

    def __new__(cls, x, y):
        return tuple.__new__(cls, (x, y))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]
    


#-----------------------------------------------------------------------------

#NamedTuple

'''
NamedTuple is the typed, class-based version of namedtuple

NamedTuple = tuple + names + type hints
'''

class PointNamedTuple(NamedTuple):
    x: int
    y: int
    
p = PointNamedTuple(3,4)

print(isinstance(p, tuple))
print(p.x) # -> 3
print(p.y) # -> 4
print(p[0]) # -> 3
print(p[1]) # -> 4

p._asdict() # {'x': 3, 'y': 4}
print(p._asdict())

p._replace(x=10)
PointNamedTuple._fields
# ('x', 'y')



