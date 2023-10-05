x = [1, 2, 3, 4]


def reverse_generator(data):
    idx = len(data) - 1

    while idx >= 0:
        yield data[idx]
        idx -= 1
        if idx == 2:
            return 'Ala ma kota'  # message do StopIteration


rg = reverse_generator(x)

print(rg)  # obiekt generatora


# for y in rg:
#     print(y)
#
# print(next(rg))
# print(next(rg))
# print(next(rg))


def gen():
    print(1)
    yield 1
    print(2)
    yield 2
    print(3)
    yield 3


# g = gen()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# generatory świetnie nadają się do obsługi streamów (danych w czasie, np. obraz na youtube)


# EDD - Event Driven Development, programowanie oparte na zdarzeniach
# Reaktive programming - czeka nie na zdarzenia, ale na zmianę streamów. Są nowe dane, to je przetwarzamy, nie ma ich, to czekamy.


# gen uuid

def gen_uuid(idx=0):
    while True:
        yield idx
        idx += 1


# d = gen_uuid()

# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))


# courutine - współprogram
# w trakcie działania generatora można wysyłać do niego dane!
def gen_magic():
    data = None
    while True:
        data = yield data


g = gen_magic()


# print(next(g))
# print(g.send('Elo tam'))
# print(next(g))


def gen_uuid2(idx=0):

    while True:
        elo = yield idx
        if elo is not None:
            idx = elo
        else:
            idx += 1


e = gen_uuid2()

print(next(e))
print(e.send(4))
print(next(e))
print(next(e))
