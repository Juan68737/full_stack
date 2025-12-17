import functools

'''
@property
'''

class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Raidus must be postitive")
    
    @radius.deleter
    def radius(self):
        del self._radius

c = Circle(5)
print(c.radius)
c.radius = 10
print(c.radius)
del c.radius


'''
@staticmethod
'''

class Math:
    @staticmethod
    def add(x,y):
        return x+y

    @staticmethod
    def multiply(x,y):
        return x*y

'''
@classmethod
'''

class Person:
    species = "Homo sapiens"

    @classmethod
    def get_species(cls):
        print(cls)
        return cls.species

print(Person.get_species())

class Student:
    count = 0

    def __init__(self, name: str, gpa: float, gender: str):
        self._name = name
        self._gpa = gpa
        self._gender = gender
        Student.count += 1

    @classmethod
    def studentCount(cls):
        print(f"There are {cls.count} students!")

s1 = Student("Jhona", 3.4, "Male")
s2 = Student("Jack", 4.0, "Male")
s3 = Student("Jackie", 3.8, "Female")
print(Student.studentCount())


'''
@functools.cache
'''

@functools.cache
def fib(n):
    if n < 2:
        return n 

    return fib(n-1) + fib(n-2)

print(fib(40))