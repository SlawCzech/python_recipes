# auto ma mieć silnik, max_speed, brand oraz accelerate, slow_down, start_engine, stop_engine

# to jest przykład factory function do tworzenia wielu obiektów
def create_auto(max_speed, brand):
    return {
        'engine': False,
        'max_speed': max_speed,
        'brand': brand,
        'actual_speed': 0
    }


def start_engine(car):
    if not car['engine']:
        car['engine'] = True
        print('Engine started.')
    else:
        print('Start engine first!')


def stop_engine(car):
    if car['speed'] == 0:
        car['engine'] = False
    else:
        print('Stop first')


def speed_up(car, amount):
    if car['engine']:
        car['actual_speed'] = min(car['actual_speed'] + amount, car['max_speed'])
        print(f"Your speed is now {car['actual_speed']}")
    else:
        print('Start engine first.')


def slow_down(car, amount):
    car['actual_speed'] = max(car['actual_speed'] - amount, 0)
    print(f"Your speed is now {car['actual_speed']}")


e47 = create_auto(308, 'BMW')
tipo = create_auto(140, 'Fiat')

print(e47)
print(tipo)


# start_engine(auto)
# speed_up(auto, 400)
#
# print(auto['actual_speed'])
