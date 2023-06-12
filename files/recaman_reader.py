import sys


# def read_series(file_path):
#     series = []
#
#     try:
#         f = open(file_path, 'rt', encoding='utf-8')
#         for line in f:
#             series.append(int(line.strip()))
#
#     finally:
#         f.close()
#
#     return series


# automatyczne zamknięcie pliku
def read_series(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


if __name__ == '__main__':
    print(read_series(sys.argv[1]))

