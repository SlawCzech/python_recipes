x = [[1, 2], [3, 4]]

y = x

print(x == y, x is y)
# True True, sprawdza wartości i czy ten sam obiekt

x[0][0] = 42

print(x, y)
# [[42, 2], [3, 4]] [[42, 2], [3, 4]]

z = x[:]  # to niekoszerne kopiowanie listy

print(z)

z = x.copy()
print(z == x, z is x)  # True False

z[0][0] = 666
print(x, y, z)  # zmieni się we wszystkich, bo tylko pierwszy poziom referencji jest skopiowany

z[0] = [1, 2]
print(x, y, z)

# Domyślna jest shallow copy, bo deep copy potrzebuje więcej zasobów, ale przede wszystkim używa rekurencji, a ta
# nie wiadomo ile razy by się wykonała (mogą być głębokie zagnieżdżenia) oraz może nastąpić nieskończona pętla, gdy
# obiekty linkują same do siebie.

from copy import deepcopy

z_deep = deepcopy(x)
print(z_deep == x, z_deep is x)  # True False

arr = [1, 2, 3]
value = 42


def magic(col, val):
    col.append(val)
    val += 10
    print(col, val)


magic(arr, value)
print(arr, value)


# [1, 2, 3, 42] 52 wykonanie funkcji zmieni wartości arr i val
# [1, 2, 3, 42] 42 poza funkcją arr jest zmienione (bo referencje), ale value nie (bo inny scope)

def magic2(col):
    col.append(value)
    value = value + 10
    print(col, value2)

magic2(arr)
print(arr, value)

# right hand side assignment, gdy po prawej stronie jest zmienna, to szuka jej w scopach LEGB
# left hand side assignment to zapis, szuka value w scope funkcji, ale nie widzi, więc tworzy zmienną i chce do siebie
# dopisać 10, ale nie może bo nie wie ile sam wynosi, więc jest błąd. Próbuje użyć zmiennej, którą dopiero tworzy!
# wpis "global value" na początku funkcji też rozwiązuje sprawę
# LHS to zapis, RHS to odczyt!!!



def add(a, b):
    return a + b

add.magic = 42
# funkcja jako obiekt

add.add = add

x = add.add.add.add.add.add.add.add(3, 4)
print(x)
# to jest ciągła rekurencja aż do momentu jak trafi na wywołanie