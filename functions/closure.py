# Closure — dostęp do zmiennych spoza aktualnie wykonywanego zasięgu

# Tworzenie:
# Minimum dwie funkcje: outer musi zwracać deklarację funkcji inner
# Funkcja inner musi korzystać z jakiegoś identyfikatora funkcji outer

# Zalety:
# Persistence (4 sposoby: closure, obiekt, generator, global)
# Typowa funkcjonalność z paradygmatu funkcyjnego

# Problemy:
# Może dojść do memory leak


# Identyfikatory przetrzymywane są w obiekcie funkcji inner

def sentence(name):
    x = 42

    def inner(age):
        return f"Mam na imię {name} i mam {age} lat."

    return inner


# print(sentence("Janusz")(42))
full_sentence = sentence("Janusz")


# print(vars(full_sentence))
# print(full_sentence.__closure__[0].cell_contents)
# print(full_sentence(42))
# print(full_sentence(33))


def uuid():
    counter = 0

    def inner():
        nonlocal counter
        result = counter
        counter += 1
        return result

    return inner


# To NIE jest closure, ale nie używa nonlocal
def uuid_():
    # counter = 0

    def inner():
        result = inner.counter
        inner.counter += 1
        return result

    # inner.counter = counter
    inner.counter = 0
    return inner


gen_uuid = uuid_()

# print(vars(gen_uuid))
# print(gen_uuid())
# print(vars(gen_uuid))
# print(gen_uuid())


# Funkcja debounce — jeżeli użytkownik nie wykona requestu w ciągu 300 milisekund, to funkcja się nie wykona,
# jeśli powyżej 300 ms to

from threading import Timer


def call_api(data):
    print(f"Response: {data}.")


def debounce(cb, delay):
    timeout_id = None

    def debounced(*args, **kwargs):
        nonlocal timeout_id

        def call_it():
            cb(*args, **kwargs)

        if timeout_id is not None:
            timeout_id.cancel()

        timeout_id = Timer(delay, call_it)
        timeout_id.start()

    return debounced


call_api_debounce = debounce(call_api, 0.3)
call_api_debounce("Janusz")
call_api_debounce("Jarosław")
call_api_debounce("Donald")


def queue():
    q = []
    return {
        'add': lambda x: q.append(x),
        'remove': lambda: q.pop(0),
        'show': lambda: q
    }


q = queue()
q['add'](1)
q['add'](2)
q['add'](3)
print(q['show']())
q['remove']()
print(q['show']())

print(q['show'].__closure__[0].cell_contents)

# Revealing module patters

# IIFE immediately invoked function expression
print((lambda: 42)())


