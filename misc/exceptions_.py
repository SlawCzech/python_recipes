# Exceptions
import io
import math
import sys


# 1. no handling of exceptions
# from random import randrange
#
#
# def main():
#     number = randrange(100)
#     while True:
#         guess = int(input('? '))
#         if guess == number:
#             print('You win!')
#             break
#
#
# if __name__ == '__main__':
#     main()

# you can pass string (like 'seven') instead of an integer and it will crash

# 2. handling exceptions
# from random import randrange
#
#
# def main():
#     number = randrange(100)
#     while True:
#         try:
#             guess = int(input('? '))
#         # catching everything also catches KeyboardInterrupt
#         # it's generally a bad idea to catch everything
#         # except:
#         # You should almost always specify an exception type
#         except ValueError:
#             continue
#         if guess == number:
#             print('You win!')
#             break


# exceptions are hierarchical and sorted by functionalities
def lookups():
    s = [1, 4, 6]

    try:
        item = s[5]
    # except IndexError:
    except LookupError:
        print('Handle index error!')

    d = {'a': 0, 'b': 1, 'c': 2}

    try:
        value = d['x']
    # except KeyError:
    except LookupError:
        print('Handle key error!')


# lookups()

# exception payloads PEP 352

def median(iterable):
    items = sorted(iterable)
    median_index = (len(items) - 1) // 2

    if len(items) == 0:
        raise ValueError('median() arg is an empty sequence.')  # this is payload (usually strings)

    if len(items) % 2 != 0:
        return items[median_index]

    return (items[median_index] + items[median_index + 1]) / 2


# print(median([1, 2, 6, 7]))
# print(median([1, 2, 6, 7, 9]))
# print(median([]))


# User defined exceptions

class TriangleError(Exception):
    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = sides

    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return f"{self.args[0]} for sides {self.sides}"

    def __repr__(self):
        return f"{type(self).__name__}({self.args[0]!r}, {self.sides!r})"


def triangle_area(a, b, c):
    sides = sorted((a, b, c))
    if sides[0] + sides[1] < sides[2]:
        raise TriangleError('Illegal triangle.', sides)

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area


# print(triangle_area(2, 4, 5))
# try:
#     print(triangle_area(2, 4, 1))
# except TriangleError as err:
#     print(err, err.sides, repr(err))


# Implicit exception chaining

def fail():
    try:
        area = triangle_area(3, 4, 10)
        print(area)
    except TriangleError as err:
        # print(err, file=sys.stdin)  # both exceptions are printed
        try:
            print(err, file=sys.stdin)
        except io.UnsupportedOperation as f:  # wyższy wyjątek jest trzymany w __context__ zagnieżdżonego
            print(err)
            print(f)
            print(f.__context__ is err)


# fail()


# Explicit exceptions chaining


class InclinationError(Exception):
    pass


def implication(dx, dy):
    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as err:
        raise InclinationError('Slope cannot be vertical.') from err


# print(implication(0, 5))


# Traceback (or stack trace czyli stos wywołań, który spowodował dojście do wyjatku)

import traceback


def fail_tb():
    try:
        implication(0, 5)
    except InclinationError as err:
        print(err.__traceback__)

        print(traceback.format_tb(err.__traceback__))  # to np idzie na systemu loggowania do dalszego przetwarzania


# fail_tb()


# Assertions - assert keyword

def modulus_four(n):
    r = n % 4
    if r == 0:
        print('Multiple of 4.')
    elif r == 1:
        print('Reminder = 1')
    else:
        assert r == 2, 'Reminder is not 2!'
        print('Reminder = 2')


# modulus_four(6)
# modulus_four(7)  # assertion error

#  python -O exceptions_.py  # odpala plik bez asercji
# w asercjach nie używamy side effectów dla bezpieczeństwa!


from bisect import bisect_left


class SortedSet:
    def __init__(self, xs):
        self._set = []
        for x in xs:
            self.add(x)

    def add(self, x):
        self._set.append(x)
        self._set = sorted(set(self._set))
        #     add invariant for bisect_left
        assert self._is_unique_and_sorted()

    def contains(self, x):
        #     add invariant for bisect_left
        assert self._is_unique_and_sorted()
        index = bisect_left(self._set, x)
        return index != len(self._set) and self._set[index] == x

    def _is_unique_and_sorted(self):
        return all(self._set[i] < self._set[i + 1] for i in range(len(self._set) - 1))


# python -m timeit -n 1 -s 'from exceptions_ import SortedSet' 's = SortedSet(range(1000))' 's.contains(10)'
# python -O -m timeit -n 1 -s 'from exceptions_ import SortedSet' 's = SortedSet(range(1000))' 's.contains(10)'


# Context manager

import contextlib
import sys

"""
Context manager stosujemy wtedy kiedy potrzebujemy zrobić przygotowanie do pewnej akcji i posprzątania po niej.
Jeżeli operacja jest podatna na błędy, to również zaleca się context managera.
"""


class LoggingContextManager:
    def __enter__(self):
        print("LoggingContextManager.__enter__()")
        return "You are in with some statement block."

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("LoggingContextManager.__exit__()", "Normal exit detected.")
        else:
            print("LoggingContextManager.__exit__()", "Exception detected.",
                  f"Type: {exc_type}, value: {exc_val}, traceback: {exc_tb}")


# Context manager usage with no exceptions
# with LoggingContextManager() as logging_ctx:
#     print(logging_ctx)

# with LoggingContextManager() as logging_ctx:
#     print(logging_ctx)
#     raise SyntaxError("Sth is no yes")

# print("See if it works.")

@contextlib.contextmanager
def logging_context_manager():
    print("Logging_context_manager: enter.")

    try:
        yield "You are in with statement block."
        print("Logging_context_manager: normal exit.")
    except Exception as e:
        print("Logging_context_manager: exceptional exit.", sys.exc_info())
        raise  # bez raise nie ma propagacji błędu wyżej


# context manager usage without exception
# with logging_context_manager() as logging_ctx:
#     print(logging_ctx)

# context manager usage with exception
# with logging_context_manager() as logging_ctx:
#     print(logging_ctx)
#     raise SyntaxError("Sth is no yes.")

# example for propagation errors
class Magic:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True  # return True blokują propagację wyjątku wyżej


# with Magic():
#     raise ZeroDivisionError("Error")
#
# print("Magic.")


# nested context managers
class Propagator:
    def __init__(self, is_propagate, name="propagator"):
        self._is_propagate = is_propagate
        self._name = name

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self._name, exc_type)
        return self._is_propagate


# with Propagator(True) as a:
#     with Propagator(True) as b:
#         raise StopIteration('No iteration.')
#
# print("Afterparty.")

# The same logic as above - one manager nested in the another
# depending on True/False configuration errors are propagated above to python or not
with Propagator(False, "a") as a, Propagator(False, "b") as b:
    raise ArithmeticError('No calculation for you.')

print('After afterparty.')
