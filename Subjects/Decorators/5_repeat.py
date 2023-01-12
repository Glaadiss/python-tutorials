def repeat(fn):
    def wrapper(*args, **kwargs):
        return [fn(*args, **kwargs) for _ in range(5)]

    return wrapper


@repeat
def say_hi():
    return "hi!"


@repeat
def add2(numb):
    return numb + 2


print(say_hi())
print(add2(3))
