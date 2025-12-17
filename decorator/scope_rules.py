
b:int = 9

def func(a: int) -> None:
    print(a)
    print(b)
    #If a variable is assigned anywhere inside a function, Python treats it as LOCAL for the entire function body.
    #b = 9

func(5)

x = 10

def read_global():
    print(x)

def write_global():
    global x
    x = 20
    print(x)


def local_example():
    y = 5
    print(y)


def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()
    inner()
    print(count)


read_global()
write_global()
read_global()

local_example()

outer()

