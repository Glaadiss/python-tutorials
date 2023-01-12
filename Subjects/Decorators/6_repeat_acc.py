from functools import reduce


def repeat(fn):
    def wrapper(*args, **kwargs):
        return [fn(*args, **kwargs) for _ in range(5)]

    return wrapper


def acc(fn):
    def wrapper(*args, **kwargs):
        arr = fn(*args, **kwargs)
        return reduce(lambda a, b: a + b, arr)

    return wrapper


@acc
@repeat
def add2(numb):
    return numb + 2


def add2_undecorated(num):
    return num + 2


print(acc(repeat(add2_undecorated))(3))
print(add2(3))
