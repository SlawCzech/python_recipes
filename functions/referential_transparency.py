# paradygmat funkcyjny

# jeżeli mamy wywołanie funkcji i w to miejsce podstawimy jej wynik, to program się zachowa tak samo


# tutaj nie jest spełnione!!
def magic():
    print('logging')
    return 42

x = magic()

# jak podstawomy x = 42, to się nie wyprintuje 'logging'
# czyli efekt nie jest taki sam

