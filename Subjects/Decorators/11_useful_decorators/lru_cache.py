from functools import lru_cache
from time import sleep


@lru_cache()
def heavy_calc(key):
    sleep(3)
    return key


print(heavy_calc(1))
print(heavy_calc(1))
