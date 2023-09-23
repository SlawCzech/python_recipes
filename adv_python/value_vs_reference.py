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