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

