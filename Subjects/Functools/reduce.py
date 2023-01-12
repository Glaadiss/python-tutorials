from functools import reduce

numbers = [3, 5, 2, 4, 7, 1]

_min = reduce(lambda a, b: a if a < b else b, numbers)
_max = reduce(lambda a, b: a if a > b else b, numbers)
_sum = reduce(lambda a, b: a + b, numbers)

print(_min, _max, _sum)

print(min(numbers), max(numbers), sum(numbers))

print("all([1, 0, 1])", all([1, 0, 1]))
print("all([1, 1, 1])", all([1, 1, 1]))
print("any([0, 1, 1])", any([0, 1, 1]))
