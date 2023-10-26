# decorator
def with_uppercase(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# function that we want to decorate
def say_hi():
    return "hello there"


say_hi_uppercased = with_uppercase(say_hi)
print(say_hi_uppercased())
