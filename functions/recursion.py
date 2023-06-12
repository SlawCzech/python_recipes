# Recursion over iteration


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# print(factorial(2))


def factorial_by_iteration(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# print(factorial_by_iteration(5))


# sumowanie listy


def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])


lst_ = [1, 2, 3, 4, 5]

# print(sum_list(lst_))


counter = 0


def fib(n):
    global counter

    counter += 1
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


# print(fib(30), counter)


# wylicz nty element ciągu Collatza


# Wybierz dowolną dodatnią liczbę całkowitą jako pierwszy wyraz ciągu.
# Jeśli dany wyraz ciągu jest parzysty, podziel go przez 2.
# Jeśli dany wyraz ciągu jest nieparzysty, pomnóż go przez 3 i dodaj 1.
# Powtarzaj kroki 2 i 3 na kolejnych wyrazach ciągu, aż do osiągnięcia wartości 1.


def collatz(n):
    print(n)
    if n == 1:
        return
    elif n % 2 == 0:
        collatz(n // 2)
    else:
        collatz(3 * n + 1)


# collatz(6)


# ciąg tribonacciego


# def tribonacci(n):
#     if n == 0:
#         return 0
#
#     elif n <= 2:
#         return 1
#
#     return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
#
#
# print(tribonacci(3))

# TODO Czemu zwraca od trzeciego


def tribonacci(n):
    sequence = [0, 0, 1]
    if n <= 2:
        return sequence[n]

    for i in range(3, n):
        next_value = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
        sequence.append(next_value)
        print(sequence)

    return sequence[n - 1]


print(tribonacci(6))
