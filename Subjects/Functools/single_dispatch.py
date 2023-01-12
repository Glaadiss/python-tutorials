from functools import singledispatch


@singledispatch
def fun(s):
    print(s)


@fun.register(int)
def _(s):
    print(s * 2)


fun("str")
fun(10)
