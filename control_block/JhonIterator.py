

class JhonIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

iter_ = JhonIterator(5)

print(next(iter_))
print(next(iter_))
print(next(iter_))
print(next(iter_))

