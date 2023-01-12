def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def say_hi():
    return "hello there"


say_hi_uppercased = uppercase_decorator(say_hi)
print(say_hi_uppercased())
