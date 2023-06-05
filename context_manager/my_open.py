import contextlib
import sys


@contextlib.contextmanager
def my_open(path, mode='r'):

    try:
        f = open(path, mode)
        yield f
    except Exception as e:
        print(sys.exc_info())
        raise
    finally:
        try:
            f.close()
        except Exception as e:
            print(e)


with my_open("example.py", "w") as file:
    file.read("x = 42")