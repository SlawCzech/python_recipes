# __iter__() zwraca obiekt iteratora


class Digits:
    def __init__(self):
        self.data = list(range(1, 11))

    def __iter__(self):
        return iter(self.data)


x = Digits()
i = iter(x)

print(next(i))
print(next(i))
print(next(i))
print(next(i))