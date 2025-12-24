from typing import TypedDict, Required, NotRequired
from typing_extensions import ReadOnly

class User(TypedDict, total = False):
    name: ReadOnly[str]
    age: int
    email: Required[str]


bob: User = {'name': 'Bob', 'age':10, 'email': 'dict@gmail.com'}

print(bob)