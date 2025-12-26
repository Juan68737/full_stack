import time
from functools import wraps
from typing import Generator,Callable, TypeVar

''''
A generator function is a function that contains yield.
When you call it, it doesn’t run immediately—it returns a generator object.
That generator object is:
    an iterator (it has __iter__ and __next__)
    lazy (computes values only when you ask for them)
    stateful (remembers where it left off between yields)

return ends the function forever

yield “pauses” and can resume later

'''

def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3


nums = (i * i for i in range(10))  # generator expression
print(next(nums))  # 0
print(next(nums))  # 1
print(next(nums))  # 2

T = TypeVar("T")

def time_init(func: Callable[..., T]) -> Callable[..., T]:
    @wraps(func)
    def wrapper(*args, **kwargs) -> T:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} init time: {end - start:.6f}s")
        return result
    return wrapper

#Why generators save memory (and sometimes time)

@time_init
def make_list():
    return [i for i in range(10_000_000)]

@time_init
def make_gen():
    return (i for i in range(10_000_000))

#make_list init time: 0.190890s
#make_gen init time: 0.000044s
lst = make_list()
gen = make_gen()



'''
The generator doesn’t hold all items—just the current state.

Time-wise: generators can be faster for pipelines because you avoid building intermediate lists.

'''

'''
Generator[yield_type, send_type, return_type]

yield_type (Y): what yield produces (what you get from next() / iteration)
send_type (S): what can be sent into the generator with .send(value)
return_type (R): what the generator “returns” when it finishes (captured in StopIteration.value)

'''


def count_up(n: int) -> Generator[int, None, None]:
    for i in range(1, n + 1):
        yield i

def count_up_v2(n: int) -> Generator[int, None, None]:
    yield from range(1,n)

def gen_list(nums: list[int]) -> Generator[int, None, None]:
    for x in nums:
        yield x

def gen_list_v2(nums: list[int]) -> Generator[int, None, None]:
    yield from nums

for n in count_up(10):
    print(n)

for n in count_up_v2(10):
    print(n)

for n in gen_list([1,2,3,4,5]):
    print(n)

for n in gen_list_v2([1,2,3,4,5]):
    print(n)

''''
IMPORTANT TL;DR

- Lists allocate and retain memory for all values at once (e.g., 10 million integers + references live simultaneously on the heap).
- Generators create one value at a time and release it before producing the next, so memory stays constant regardless of sequence size.

'''
