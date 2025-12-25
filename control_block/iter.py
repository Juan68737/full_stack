from typing import List, Iterable, Iterator


names: List[str] = ['Jhonathan', 'John', 'Juan']
namesIter: Iterator[str] = iter(names)

print(next(namesIter))
print(next(namesIter))
print(next(namesIter))


colors: List[str] = ['Blue', 'Red', 'Yellow']
cars: set[str] = {'Tesla', 'BMW', 'Nissan'}


def iterAll(itr: Iterable[str]):
    for i in itr:
        print(f'Printing: {i}')

print("-----------")
iterAll(colors)
print("-----------")
iterAll(cars)
print("-----------")



