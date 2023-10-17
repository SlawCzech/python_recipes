# class X:
#     def __new__(cls, data):
#         if data != 42:
#             raise ValueError('Sth is no yes!')
#
#         cls.do_magic = lambda self, value: self.data * value
#         self = super().__new__(cls)
#         return self
#
#     def __init__(self, data):
#         self.data = data
#
#
# try:
#     x = X(42)
# except ValueError as e:
#     # custom logic
#     pass
# except TypeError as e:
#     # custom logic
#     pass
# else:
#     print('kiedy to działa?')
# finally:
#     print('zawsze')
#
# print(x)
import random


# ma możliwość zrobienia temperatury -> 1 arg do konstruktora -> jest w celsius
# ma możliwość zrobienia temperatury -> 2 arg do konstruktora -> pierwszy to ilość, drugi to jednostka


class Temperature:
    def __new__(cls, temp):
        self = super().__new__(cls)
        self.temp = f'{temp} C'
        return self

    @classmethod
    def temp_with_unit(cls, temp, unit):
        self = super().__new__(cls)
        self.temp = f'{temp} {unit}'
        return self

    @staticmethod
    def do_sth_awesome():
        greetings = [
            f"Witaj, mój Panie!",
            f"Pięknie dzisiaj wyglądasz.",
            f"Co jeszcze mogę dla Ciebie zrobić?"
        ]
        return random.choice(greetings)


x = Temperature(34)
print(x.temp)

y = Temperature.temp_with_unit(34, 'k')
print(y.temp)

print(Temperature.do_sth_awesome())
print(x.do_sth_awesome())