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


# print(hello('Mateusz'))
# print(bye('Mateusz', "M."))


def change_letters(fn):
    def inner(name):
        return fn(name.title())

    return inner


def reverse_name(fn):
    def inner(name):
        return fn(name[::-1])

    return inner


def upper(fn):
    def inner(name):
        return fn(name).title()

    return inner


def html(fn):
    def inner(name):
        hej, name = fn(name).split()

        return f'<p>{hej}<h2> {name} </h2></p> '

    return inner


@change_letters
@reverse_name
def sentence(name):
    return f'Hello {name}.'


# print(sentence('janusz'))


@html
@upper
def message(name):
    return f'hello {name}'


@html
@upper
def bye_message(name):
    return f'Bye {name}'


#
# print(message('janusz'))
# print(bye_message('janusz'))

import webbrowser


def html_template(filename):
    def wrapper(fn):
        def inner(name):
            return fn(name)

        return inner

    return wrapper


def tag(hdl, **kwargs):
    def wrapper(fn):
        def inner(name):
            greeting, name = fn(name).title().split(' ')
            attributes = ' '.join([f'{attr}="{value}"' for attr, value in kwargs.items()])
            tag_with_attrs = f'<{hdl} {attributes}>{name}</{hdl}>'
            with open('index.html', 'w') as f:
                f.write(f'<p>{greeting} {tag_with_attrs}</p>')
            return webbrowser.open('index.html')

        return inner

    return wrapper


@html_template("index.html")
@tag("h2", style="red")
def message(name):
    return f'hello {name}'


@html_template("index.html")
@tag("h3", className="elo")
def bye_message(name):
    return f'bye {name}'


# napisz generator html -> <p>Hello <h2 class="name" style="color: red;">Janusz</h2></p>
# napisz dekorator, który w momencie wywołania funkcji message wstawi zwrócony html na stronę internetową
# print(message('Janusz'))


# print(bye_message('Janusz'))
from datetime import time

# napisz dekorator, który automatycznie będzie memoizował funkcję. jak skończysz sprawdź czym jest lru_cache.
import time


def memo(fn):
    _cache = {}

    def inner(*args, **kwargs):
        key = " ".join(str(char) for char in args) + " ".join(f'{k, v}' for k, v in kwargs.items())
        if key not in _cache:
            _cache[key] = fn(*args, **kwargs)
        return _cache[key]

    return inner


@memo
def magic(a, b):
    time.sleep(5)
    print('już to mam')
    return a + b


@memo
def multiply(a, b):
    time.sleep(5)
    print('już już')
    return a * b


magic(1, 2)
magic(2, 1)
magic(1, 2)
multiply(1, 2)
