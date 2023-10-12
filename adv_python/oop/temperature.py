# pełna implementacja @property

# class Temperature:
#     def __init__(self, temperature):
#         self.temperature = temperature
#
#     def get_temperature(self):
#         print('getter')
#         # formatowanie outputu
#         return f'{self._temperature} C'
#
#     def set_temperature(self, value):
#         # walidacja danych (ale to się da obejść!)
#         print('setter')
#         self._temperature = value
#
#     def del_temperature(self):
#         # teardown - sprawdzamy czy gdzieś nie jest wykorzystywane i dopiero potem usunięcie
#         print('deleter')
#         del self._temperature
#
#     temperature = property(get_temperature, set_temperature, del_temperature)


class Temperature:
    def __init__(self, temp_c):
        self.temp_c = temp_c

    @property
    def temp_c(self):
        return f'{self._temperature} C'

    @temp_c.setter
    def temp_c(self, value):
        if value < -273.15:
            raise ValueError('Too cold!')
        self._temperature = value

    @property
    def temp_f(self):
        return f'{self._temperature * 9 / 5 + 32} F'

    @temp_f.setter
    def temp_f(self, new_temp):
        self.temp_c = (new_temp - 32) * 5 / 9

    @property
    def temp_k(self):
        return f'{self._temperature + 273.15}'

    @temp_k.setter
    def temp_k(self, new_temp):
        self.temp_c = new_temp - 273.15

    def __repr__(self):
        attrs = ', '.join(f'{k[1:] if k.startswith("_") else k}={v!r}' for k, v in vars(self).items())
        return f'{type(self).__name__}({attrs})'

    def __str__(self):
        return f"{self.temp_c}"

    def __format__(self, format_spec):
        # units = {'c': self.temp_c, 'f': self.temp_f, 'k': self.temp_k}
        # return units.get(format_spec, self.temp_c)
        if format_spec == 'f':
            return self.temp_f
        elif format_spec == 'k':
            return self.temp_k
        else:
            return self.temp_c


t = Temperature(-30)
# t.temp_k = 1
# print(t.temp_c)
# print(t.temp_f)
# print(t.temp_k)
# t._temperature = 666
# print(vars(t))
# print(dir(t))
print(str(t))
print(repr(t))
print(f'{t:c}')
print(f'{t:f}')
print(f'{t:k}')


class MarsTemperature(Temperature):
    pass


mt = MarsTemperature(2137)
print(str(mt))
print(repr(mt))
