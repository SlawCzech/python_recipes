import sys

# Funkcja open zwraca iterator po linijce
# print dorzuca enter, sys.stdout nie robi tego

f = open(sys.argv[1], 'rt', encoding='utf-8')

for line in f:
    # print(line)
    sys.stdout.write(line)

f.close()

