# służą do generowania kolekcji: lista, set, słownik
# generator comprehension ma taką samą składnię, ale nie generuje kolekcji (taki bardziej iterator)
from pprint import pprint
from random import randint

# 1. list comprehension
# [x for x in iterable]
# aggregate([map for item in iterable if filter])

x = [1, 2, 3, 4]
sum(item * 2 for item in x if item % 2)


data = [[1, 2], [3, 4]]

result = [[y * 3 for y in x] for x in data if sum([y * 3 for y in x]) < 10]

# print(result)

# flatten data variable

effect = [y for x in data for y in x]

# print(effect)

for y in data:
    for x in y:
        print(x)


# Set comprehension

# taki sam jak list comprehension, ale z klamerkami
# {x for x in iterable}

x = [randint(1, 10) for _ in range (1000)]

# print(len(x))

z = {y * randint(1, 500) for y in x}

# print(len(z))

# Dict comprehension

# tak jak set comprehension, ale jest para klucz-wartość

capital_cities = {
    'Warsaw': 'Poland',
    'Berlin': 'Germany',
    'Paris': 'France',
    'London': 'United Kingdom',
    'Madrid': 'Spain',
    'Istanbul': 'Germany',
}

new_dict = {capital.lower(): country[:-1].lower() + country[-1].upper() for capital, country in capital_cities.items()}

# print(new_dict)
capital_modified = {country: capital for capital, country in capital_cities.items()}

# print(capital_modified)

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']

words_modified = {key: [c for index, c in enumerate(key) if key.count(c, 0, index) < 1] for key in words}

# print(words_modified)

# Samolot ma 25 rzędów, siedzenia są ABCDEG.
# Napisz listę słowników, gdzie kluczem jest nazwa siedzenia, a rząd indeksem.

seats = 'ABCDEG'

airplane = [{seat: None for seat in seats} for _ in range(25)]

pprint(airplane)


# Generator expression

# służy do wygenerowania iteratora (generatora)
# nawiasy nie w każdy przypadku są konieczne
# jest lazy evaluated, czyli obliczenia są wykonywanie na żądanie
# nie jest super szybki, ale generuje tylko to, co aktualnie potrzebujemy


words_2 = ['apple', 'banana', 'cherry', 'date', 'elderberry', 35]

result_2 = " ".join(str(word) for word in words_2)  # to jest generator expression, czyli iterable

result_3 = (str(word) for word in words_2)
print(next(result_3))
print(next(result_3))
