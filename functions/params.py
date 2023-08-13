# Parametry są w deklaracji funkcji, a argumenty w wywołaniu funkcji

# Parametry mogą być pozycyjne, nazwane i opcjonalne (default)

def add(a, b):
    return a + b


add(1, 2)
add(1, b=2)
# add(a=1, 2) ERROR! pozycyjne przed nazwanymi
add(a=1, b=2)
add(b=2, a=1)

x = [1, 2]
add(*x)
y = {'a': 1, 'b': 2}
add(**y)
add(*(lambda: (1, 2))())


def magic(a, b, /, c, d, *, e, f):
    pass


# Przed slashem tylko pozycyjne, po gwiazdce tylko nazwane!! między nimi pozycyjne lub nazwane.
# w pythonie głównie używa się go zagwarantowania tego samego API dla funkcjonalności z innych języków (C++)
# przykład z pythona: range.


# parametry defaultowe
# nie używaj parametrów mutowalnych jako domyślnych!!
def do_sth(item, col=[]):
    col.append(item)
    return col


# prawidłowa implementacja:
def so_sth_right(item, col=None):
    if col is None:
        col = []
    col.append(item)
    return col


print(do_sth(1))
print(do_sth(2, []))
print(do_sth(42))


# niewiadoma ilość parametrów
def infinite_params(*args, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

#
# infinite_params()
# infinite_params(1, 2)
# infinite_params(a=1, b=2)
# infinite_params(3, 4, a=1, b=2)


# napisz funkcję html, która jako pierwszy parametr przyjmie tekst, drugi to nazwa znacznika, a trzeci to atrybuty znacznika

def create_tag(text, tag_name, **attrs):
    attrs = " ".join(f'{key}="{value}"' for key, value in attrs.items())
    return f'<{tag_name} {attrs}>{text}<{tag_name}>'


print(create_tag('ala ma kota', 'h1', id='test', style='color: red;'))
