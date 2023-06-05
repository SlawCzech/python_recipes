# służą do generowania kolekcji: lista, set, słownik

# 1. list comprehension
# [x for x in iterable]
# aggregate([map for item in iterable if filter])

x = [1, 2, 3, 4]
sum(item * 2 for item in x if item % 2)


data = [[1, 2], [3, 4]]

result = [[y * 3 for y in x] for x in data if sum([y * 3 for y in x]) < 10]

print(result)

# flatten data variable

effect = [y for x in data for y in x]

print(effect)

for y in data:
    for x in y:
        print(x)
