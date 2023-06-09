# Niemodyfikowalność

# zajmuje tylko tyle miejsca ile jest potrzebne (a nie jak np. lista)
# sprawdzić dokumentację jak się alokuje extra miejsce

# poprawa efektywności działania kodu (mniej operacji do wykonania, np sprawdzania typu danych).
# nie trzeba sprawdzać czy coś się zmieniło

from copy import deepcopy

s = 'hello'
# print(id(s))
s = s + ' world'


# print(id(s))

# print(s)


# TODO zweryfikować ID dla liczb powyżej pewnego zakresu


# jak osiągnąć niemutowalność w pytonie
# dzięki deepcopy osiągamy niemutowalność np. list


def filter_list(lst):
    # return [x * 2 for x in lst if len(x) < 6]
    lst_ = deepcopy(lst)
    lst_[0][0] = 42
    return lst_


x = ['1', '2', '3', 'jdhfksurhkn']

y = [['elo', 'tam'], [1, 2, 3]]

print(filter_list(y), y)


