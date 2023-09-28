# dekoratory to funkcjonalność w pythonie, ale też wzorzec projektowy (to nie to samo)
# funkcjonalność:
# - modyfikuje lub dodane nowe funkcjonalności do funkcji/metody/klasy
# - dekoratory funkcji lub metody tworzymy dzięki closure lub podwójnego closure
# - dekoratory klasy nie tworzy się z closure, to coś jak metaklasy


def add_greeting(fn):
    def inner(*args):
        result = f'Hello {fn(*args)}'
        return result

    return inner


@add_greeting
def hello(name):
    return name


@add_greeting
def bye(name, surname):
    return f'{name} {surname}'


print(hello('Mateusz'))
print(bye('Mateusz', "M."))
