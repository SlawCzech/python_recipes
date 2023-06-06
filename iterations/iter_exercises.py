from functools import reduce

data = [
    {
        'name': 'Paweł',
        "age": 38,
        "city": 'Kraków',
        "hobbies": ['python', 'deep learning', 'big data']
    },
    {
        "name": "Sławek",
        "age": 40,
        "city": "Katowice",
        "hobbies": ["deep drinking", "big hot dogs", "all night partying"]
    },
    {
        "name": "Martyna",
        "age": 35,
        "city": "Olsztyn",
        "hobbies": ["crocheting", "sewing", "eating"]
    },
    {
        'name': 'Rafał',
        'age': 43,
        'city': 'Będzin',
        'hobbies': ['python', 'sport', 'alkohol']
    },
    {
        "name": "Błażej",
        "age": 48,
        "city": "Ełk",
        "hobbies": ["python", "literature", "gym"]
    },
    {
        "name": 'Maciej',
        "age": 27,
        "city": "Warszawa",
        "hobbies": ['programming', 'gaming', 'reading'],
    },
    {
        "name": "BartekS",
        "age": 38,
        "city": "Kraków",
        "hobbies": ["reading", "gaming", "skiing"]
    },
    {
        'name': 'Anna',
        'age': 36,
        'city': 'Warszawa',
        'hobbies': ['python', 'django', 'restapi']
    },
    {
        'name': 'bartek',
        'age': 30,
        'city': 'katowice',
        'hobbies': ['python', 'sport', 'games']
    },
    {
        "name": "Adrian",
        "age": 37,
        "city": "Mysłowice",
        "hobbies": ["reading", "history", "yawning"]
    },
    {
        "name": 'Michał',
        "age": 23,
        "city": "Katowice",
        "hobbies": ["stock market", "football", "books"]
    },
]

# Impreza tam, gdzie jest najwięcej osób

cities = {item['city'] for item in data}
# print(cities)

zones = {'north': ['Olsztyn', 'Ełk', 'Warszawa'],
         'south': ['Kraków', 'Katowice', 'Będzin', 'Mysłowice', 'katowice'],
         }

# klasyk

counter_s = 0
counter_n = 0

for person in data:
    if person['city'] in zones['north']:
        counter_n += 1
    else:
        counter_s += 1

# print(counter_n)
# print(counter_s)

party = {key: len([person["city"] for person in data if person["city"] in value]) for key, value in zones.items()}

print(party)

# map, filter, reduce

party_2 = map(lambda x: sum(map(lambda y: y['city'] in x, data)), zones.values())

print(list(party_2))

# map przyjmuje nieskończenie wiele parametrów

x = [1, 2, 3]
y = [1, 2, 3]
z = [1, 2, 3]

# przygotuję ITERTOOLS
# chodzi o zip

sum_lists = list(map(lambda a, b, c: a + b + c, x, y, z))

print(sum_lists)
