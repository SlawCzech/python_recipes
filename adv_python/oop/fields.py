class X:
    magic = 42

    def __init__(self, new_magic):
        # pola klasy modyfikujemy tylko przez klasę, bo inaczej stworzy się pole obiektu, które przysłoni pole klasy
        # Użyj type(self), który zwróci stosowną klasę!
        # self.magic = new_magic
        type(self).magic = new_magic

    def get_magic(self):
        return self.magic

    @property
    def magic(self):
        return self._magic

    @magic.setter
    def magic(self, value):
        self._magic = value


class Y(X):
    magic = 666


x = X(2137)
# tworzy pole obiektu, a nie modyfikuje pola klasy, co zepsuje share stan
x.magic = 666
# print(X.magic)
# print(x.magic)
# print(x.get_magic())

y = Y(42)

print(Y.magic)
print(y.magic)

# print(vars(X))
