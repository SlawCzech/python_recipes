# Iterable

class CustomIterable:
    def __init__(self, start, stop, step):
        self._data = list(range(start, stop, step))

    def __iter__(self):
        return iter(self._data)


fancy_collection = CustomIterable(1, 10, 2)


# print(fancy_collection)

# for item in fancy_collection:
#     print(item)


# print(iter(fancy_collection))

# iterator definiuje który element będzie następny, dlatego może być customowy, tj. iterator to nie iterable!!

class Array:
    def __init__(self, iterator):
        self._data = list(range(11))
        self._iterator = iterator

    def __iter__(self):
        return self._iterator(self._data)


class EveryThird:
    def __init__(self, data):
        self._data = data
        self._counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._data) <= self._counter:
            raise StopIteration

        result = self._data[self._counter]
        self._counter += 3
        return result


class Odd:
    def __init__(self, data):
        self._data = data
        self._counter = 0

    def __iter__(self):
        return iter(self)

    def __next__(self):
        if len(self._data) <= self._counter:
            raise StopIteration

        for item in self._data[self._counter:]:
            self._counter += 1
            if item % 2 != 0:
                return item

        raise StopIteration  # jak już nie ma elementów w pętli


every_third_items = Array(EveryThird)

odd_items = Array(Odd)

for item in every_third_items:
    print(item)

print('x' * 20)
print()
print('x' * 20)

for item in odd_items:
    print(item)

# wrócić do trawersowania po drzewach binarnych!!!!!
