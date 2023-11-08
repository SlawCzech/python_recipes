import operator


def my_count(start=0, step=1):
    while True:
        yield start
        start += step


class MyCounter:
    def __init__(self, start=0, step=1):
        self._step = step
        self._start = start

    def __iter__(self):
        return self

    def __next__(self):
        result = self._start
        self._start += self._step
        return result


# count = MyCounter()
# print(next(count))
# print(next(count))
# print(next(count))
# print(next(count))


class MyCycle:
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._iterable) == 0:
            raise StopIteration

        result = self._iterable[self._index % len(self._iterable)]
        self._index += 1

        return result


class MyRepeat:
    def __init__(self, element, n=True):
        self._n = n
        self._element = element

    def __iter__(self):
        return self

    def __next__(self):
        while self._n:
            if self._n is not True:
                self._n -= 1

            return self._element
        raise StopIteration


class MyAccumulate:
    def __init__(self, iterable, func=operator.add, *, initial=None):
        self._iterable = [initial] + iterable if initial else iterable
        self._acc = iterable[0]
        self._func = func
        self._index = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._iterable):
            raise StopIteration

        result = self._acc

        self._acc = self._func(self._acc, self._iterable[self._index])
        self._index += 1

        return self._acc
