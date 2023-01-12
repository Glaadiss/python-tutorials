import logging

logger = logging.getLogger()

"""
Write decorator with name `logged` that adds logging functionality to add and spam functions
Remove add and spam functions and uncomment decorated `add` and `spam` functions
Ensure that tests still pass
"""


def add(x, y):
    value = x + y
    logger.log(logging.DEBUG, value)
    return value


def spam():
    value = "spam"
    logger.log(logging.CRITICAL, value)
    return value


# @logged(logging.DEBUG)
# def add(x, y):
#     return x + y


# @logged(logging.CRITICAL)
# def spam():
#     return "spam"
