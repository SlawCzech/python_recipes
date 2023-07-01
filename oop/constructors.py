# Założenie, że funkcja jest wywoływana jako metoda.
# Pierwszy parametr to obiekt


def learn(self, language):
    # sprawdzenie czy klasa obiektu posiada dany atrybut
    if hasattr(type(self), "languages"):
        type(self).languages.append(language)
    else:
        type(self).languages = [language]


class Programmer:
    def __new__(cls, *args, **kwargs):
        # ta linijka musi się zawsze znaleźć jeśli nadpisujemy domyślny __new__ z klasy object
        self = super().__new__(cls)
        # dynamiczne dodawanie pola obiektu
        if args[0] > 10:  # czy skill > czy < od 10, to się ustawia magic lub nie
            self.magic = 42  # przypisanie pola obiektu przed initem
        # cls.my_magic = lambda self, value: value * 2  # przypisanie metody klasy przed initem
        # cls.learn = learn  # przypisanie metody klasy, ale tak się generalnie nie robi
        # dodawanie atrybutu do klasy
        setattr(cls, "my_magic", lambda self, value: value * 2)  # tak się robi :)
        setattr(cls, "learn", learn)  # i tak się robi :)
        print("__new__")

        return self  # to dostanie __init__!!

    def __init__(self, skill):
        self._skill = skill
        print("__init__")


# p = Programmer(12)
#
# print(vars(p))
# print(dir(p))
# print(p.my_magic(4))
# p.learn('java')
# p.learn('html')
# print(p.languages)


class GalacticMagic:
    pass


class Magic:
    def __new__(cls, *args, **kwargs):
        return GalacticMagic()  # konstruktor klasy Magic zwraca obiekt innej klasy


# m = Magic()
# print(type(m))


class VideoPlayer:
    pass


class MusicPlayer:
    pass


class Player:  # klasa Player może zwracać trzy różne obiekty
    def __new__(cls, *args, **kwargs):
        if kwargs.get("type") == "music":
            self = MusicPlayer()
        elif kwargs.get("type") == "video":
            self = VideoPlayer()
        else:
            self = super().__new__(cls)
        setattr(self, "_duration", kwargs.get("duration"))
        return self

    def __init__(self, *, duration):
        self._duration = duration


# Player.__new__(Player)
# Player.__init__(player)

# player_m = Player(type="music", duration=9)
# print(type(player_m), player_m._duration)
#
# player_v = Player(type="video", duration=10)
# print(type(player_v), player_v._duration)
#
# player = Player(duration=12)
# print(type(player), player._duration)

#
# class X:
#     def make_magic(self):
#         return 42
#
#
# x = X()
# print(x.make_magic())
# print(X.make_magic(x))


# obiekt, który można stworzyć dwoma lub trzema parametrami
class Car:
    def __init__(self, model, fuel):
        self._model = model
        self._fuel = fuel

    @classmethod
    def make_electric_car(cls, model, fuel, distance):
        self = cls(model, fuel)
        self._distance = distance
        return self


# car = Car('astra', 'gas')
# print(vars(car))
# electric_car = Car.make_electric_car('mustang', 'Strom', 150)
# print(vars(electric_car))


# Singleton by custom constructor


class Single:
    single_instance = None

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def create_class_object(cls, *args, **kwargs):
        if cls.single_instance is None:
            cls.single_instance = cls(*args, **kwargs)

        return cls.single_instance


sin = Single.create_class_object()

second_sin = Single.create_class_object()

# print(sin is second_sin)

s1 = Single()
s2 = Single()


# print(s1 is s2)


# Klasy dziedziczące są też singletonami

class MotherOfSingletons:
    instances = {}

    def __new__(cls, *args, **kwargs):
        if cls.instances.get(cls) is None:
            cls.instances[cls] = super().__new__(cls)
        return cls.instances[cls]


class InheritedSingleton(MotherOfSingletons):
    pass


class OneMoreSingleton(MotherOfSingletons):
    pass


i1 = InheritedSingleton()
i2 = InheritedSingleton()
o1 = OneMoreSingleton()
o2 = OneMoreSingleton()
#
# print(i1 is i2)
# print(o1 is o2)
# print(i1 is o2)


# stwórz klasę, która będzie rozpoznawać typy parametrów (int * 2, string -> lower)
from functools import singledispatchmethod


class ParametersType:
    @singledispatchmethod
    def __init__(self, parameter_one, parameter_two):
        self.parameter_one = parameter_one
        self.parameter_two = parameter_two

    @__init__.register
    def _(self, parameter_one: str, parameter_two: str):
        self.parameter_one = parameter_one.lower()
        self.parameter_two = parameter_two.upper()

    @__init__.register
    def _(self, parameter_one: int, parameter_two: int):
        self.parameter_one = parameter_one * 2
        self.parameter_two = parameter_two * 2


s1 = ParametersType('first', 'second')
s2 = ParametersType(3, 6)


#
# print(vars(s1))
# print(vars(s2))


class Calculator:
    @singledispatchmethod
    def add(self, a, b):
        raise TypeError('Incorrect types.')

    @add.register
    def _(self, a: int, b: int):
        return a + b

    @add.register
    def _(self, a: str, b: str):
        return int(a) + int(b)


calc = Calculator()

# print(calc.add(2, 3))
#
# print(calc.add("3", "6"))


# __call__ umożliwia wywoływanie obiektów


class Calculator2:
    def __call__(self, a, b):
        return a + b


calc2 = Calculator2()

# print(calc2(3, 4))


# metaclass pseudokod
#
#
# class MetaX:
#     def __call__(self, *args, **kwargs):
#         s = self.__new__(*args, **kwargs)
#         self.__init__(s, *args, **kwargs)
#
#         return s


# po princie objectu ma zwrócić swoją wartość (np. 5), a przy wywołaniu ma dodać do siebie  wartość
# print(x) -> 5
# x(15) -> 20


class SuperInt(int):
    def __init__(self, value):
        self._value = value

    def __call__(self, other_value):
        self._value += other_value
        return self._value


sint = SuperInt(5)
# print(vars(sint))
print(sint(3) + 42)
print(sint(7))

