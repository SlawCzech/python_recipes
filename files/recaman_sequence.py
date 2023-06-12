import sys
from itertools import count, islice


def sequence():
    """Generate Recaman's sequence."""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


# seq = sequence()

# print(next(seq))
# print(next(seq))


# def write_sequence(file_path, num):
#     f = open(file_path, 'wt', encoding='utf-8')
#     f.writelines(f'{r}\n' for r in islice(sequence(), int(num) + 1))
#     f.close()


# automatyczne zamknięcie pliku
def write_sequence(file_path, num):
    with open(file_path, 'wt', encoding='utf-8') as f:
        f.writelines(f'{r}\n' for r in islice(sequence(), int(num) + 1))


if __name__ == '__main__':
    write_sequence(file_path=sys.argv[1], num=sys.argv[2])

