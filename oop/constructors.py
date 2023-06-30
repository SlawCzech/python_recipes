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
        setattr(cls, "learn", learn)  # i ta się robi :)
        print("__new__")

        return self  # to dostanie __init__!!

    def __init__(self, skill):
        self._skill = skill
        print("__init__")


p = Programmer(12)

print(vars(p))
print(dir(p))
print(p.my_magic(4))
p.learn('java')
p.learn('html')
print(p.languages)
