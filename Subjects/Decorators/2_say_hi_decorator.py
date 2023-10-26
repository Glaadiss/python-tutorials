def with_uppercase(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@with_uppercase
def say_hi():
    return "hello there"


print(say_hi())
