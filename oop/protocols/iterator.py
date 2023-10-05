import random


class WhenTheRoosterCrowsThreeTimes:
    def __init__(self, data):
        self._data = data
        self._counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._counter > 2 or len(self._data) == 0:
            print('Betray Me')
            raise StopIteration

        result = random.choice(self._data)
        self._counter += 1

        return result


rooster = [1, 2, 3, 4, 5, 6]
rooster2 = []

betray = WhenTheRoosterCrowsThreeTimes(rooster)


# betray = WhenTheRoosterCrowsThreeTimes(rooster2)

# for b in betray:
#     print(b)


class Iterable:
    def __init__(self, data, iterator):
        self._data = data
        self._iterator = iterator

    def __iter__(self):
        return self._iterator(self._data)


class ReverseIterator:
    def __init__(self, data):
        self._data = data
        self.idx = len(self._data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < 0:
            print('End of iteration')
            raise StopIteration

        result = self._data[self.idx]
        self.idx -= 1

        return result


class OddIterator:
    def __init__(self, data):
        self._data = data
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self._data):
            if self._data[self.idx] % 2:
                result = self._data[self.idx]
                self.idx += 1
                return result
            else:
                self.idx += 1

        raise StopIteration


i = Iterable([1, 2, 3, 4, 5, 6, 7, 8, 9], OddIterator)

for x in i:
    print(x)


# generator to po prostu lepsza składnia interatora

