class Monad:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        return func(self.value)

    def __str__(self):
        return str(self.value)


def monad(value):
    def bind(func=None):
        if func is not None:
            bind.value = func(value)
        return bind

    bind.value = value
    return bind


def add_one(x):
    return Monad(x + 1)


def add_two(x):
    return monad(x + 2)()


def multiply_by_three(x):
    return monad(x * 3)()


# result = Monad(3).bind(add_one).bind(multiply_by_two)

result = monad(3)(add_two)(multiply_by_three).value  # nie działa

print(vars(result))


def monade(value, func):  # prototyp dla monady
    return func(value)


# paczka PyMonad można się pobawić