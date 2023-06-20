# GENERATORS
# składnia domyślna jako funkcja
# staje się generatorem jak ma przynajmniej jedno słówko yield
# lazy evaluated
# używane po to, żeby łatwiej tworzyć iteratory
# każdy iterator da się zapisać generatorem

def gen():
    print(1)
    yield 1
    print(2)
    yield 2
    print(3)
    # tu jest domyślny return jako StopIteration


g = gen()

# print(g)
# print(next(g))
# print(next(g))
# print(next(g))


# napisz generator liczb od 1 do nieskończoności:


def infinity():
    counter = 1
    while True:
        yield counter
        counter += 1
        if counter > 3:  # kończy iterację gdy counter = 3
            return


infin = infinity()

# print(infin)
# print(next(infin))
# print(next(infin))
# print(next(infin))
# print(next(infin))


# TO JEST KORUTINA coroutine (współprogram)
# taka sama składnia jak generator
# korutina może przyjmować dane podczas runtime

def magic():
    a = 10
    b = yield a + 20   # yield jest możliwe po prawej stronie!! mimo że do de facto jest return
    yield b


m = magic()

print(next(m))
print(m.send("hello"))
# print(next(m))
# print(next(m))
# print(next(m))
# print(next(m))