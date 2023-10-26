from contextlib import contextmanager


@contextmanager
def read_numbers(name):
    f = open(name, "r")
    print("2")
    try:
        rows = f.read().split("\n")
        yield [int(r) for r in rows if r != ""]
        print("4")
    finally:
        print("5")
        f.close()


print("1")

with read_numbers("Subjects/ContextManager/demo.txt") as o:
    print("3")
    print("result", o)

print("6")
