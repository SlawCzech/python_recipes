class Auto:
    def __init__(self, brand, max_speed):
        self.actual_speed = 0
        self.engine = False
        self.max_speed = max_speed
        self.brand = brand

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print('Engine started.')
        else:
            print('Start engine first!')

    def stop_engine(self):
        if self.actual_speed == 0:
            self.engine = False
        else:
            print('Stop first')

    def speed_up(self, amount):
        if self.engine:
            self.actual_speed = min(self.actual_speed + amount, self.max_speed)
            print(f"Your speed is now {self.actual_speed}")
        else:
            print('Start engine first.')

    def slow_down(self, amount):
        self.actual_speed = max(self.actual_speed - amount, 0)
        print(f"Your speed is now {self.actual_speed}")


e47 = Auto('BMW', 308)
tipo = Auto('Fiat', 140)

Auto.speed_up(e47, 200)

e47.speed_up(200)