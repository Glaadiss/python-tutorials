import atexit


@atexit.register
def goodbye():
    print("Bye bye!")


print("Hello Yang!")
