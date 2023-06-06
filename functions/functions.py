# Deklaracja funkcji

def add(a, b):
    # function body
    return a + b


# def - keyword (słowo klucz)
# add - identyfikator (nazwa funkcji) zgodny z PEP8. Małe litery, słowa rozdzielone underscore, nie może zaczynać się od
# cyfry, dopuszczalne znaki: litery, cyfry, underscore. nazwa: musi być akcją (funkcja ma coś robić), deskryptywna
# (ma opisywać, co robi), powinna być po angielsku
# () - wymagane
# : - wcięcie w większości przypadków, wyjątki: lambda, typowanie, klucz:wartość w słowniku, if
# ciało funkcji — zbiór instrukcji
# return, zwraca zawsze wynik operacji, która jest zaraz po jego prawej stronie. Domyślnie zwraca None. Funkcja może
# zwrócić tylko jedną rzecz
# deklarację funkcji tworzy się raz, ale wywołań może być wiele

# wywołanie funkcji
add(2, 4)

# Funkcja jest obiektem
# Obiekt przechowuje pewne cechy i funkcjonalności. Zachowuje się jak obiekt: dot notation.
# vars(add) sprawdza właściwości obiektu
# dir(add) sprawdza metody obiektu
# funkcje w python są First Class Citizen — oznacza to, że są obiektami.
# Higher Order Function — może przyjąć jako parametr deklarację innej funkcji lub zwrócić deklarację funkcji


def upper(text):
    return text.upper()


# Higher Order Function (m.in. map, filter, reduce)
def sentence(callback, text):
    return callback(text)


# Kompozycja: jeśli dany obiekt przyjmuje inny obiekt jako parametr, to możemy modyfikować działanie pierwszego obiektu.
# np. w klasach, gdy pole klasy może mieć przypisane obiekty różnych klas


def reverse(text):
    return text[::-1]


def capitalize(text):
    return text.capitalize()

# sentence będzie miał inne działanie w zależności od callbacka
print(sentence(reverse, 'Ala ma kota'))
print(sentence(capitalize, 'Ala ma kota'))
print(sentence(reverse, sentence(capitalize, 'ala ma kota')))
print(sentence(capitalize, sentence(reverse, 'ala ma kota')))
