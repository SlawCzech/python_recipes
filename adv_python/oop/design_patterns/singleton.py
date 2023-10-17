

class Singleton:

    _cache = {}

    def __new__(cls, *args, **kwargs):
        if cls not in Singleton._cache:
            Singleton._cache[cls] = super().__new__(cls, *args, **kwargs)
        return Singleton._cache[cls]


class X(Singleton):
    pass


class Y(Singleton):
    pass


x1 = X()
x2 = X()

print(x1 is x2)

y = Y()
print(x1 is y)
