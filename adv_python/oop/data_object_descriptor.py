class Auto:
    def __init__(self, speed):
        self.speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        if new_value < 0:
            raise ValueError('Sth is no yes')
        self._speed = new_value

    def speed_up(self, new_speed):
        self.speed = new_speed


a = Auto(10)
print(a.speed)
