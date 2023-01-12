from functools import reduce, wraps


def repeat(times):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return [fn(*args, **kwargs) for _ in range(times)]

        return wrapper

    return inner


def acc(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        arr = fn(*args, **kwargs)
        return reduce(lambda a, b: a + b, arr)

    return wrapper


@acc
@repeat(5)
def add2(numb):
    """add 2 to the number"""
    return numb + 2


def add2_undecorated(num):
    """add 2 to the number"""
    return num + 2


print(acc(repeat(5)(add2_undecorated))(3))
print(add2(3))


print(
    "add2",
    add2.__doc__,
    add2.__name__,
)

print(
    "add2_undecorated",
    add2_undecorated.__doc__,
    add2_undecorated.__name__,
)
