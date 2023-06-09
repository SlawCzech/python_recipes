# Currying - konwersja funkcji na funkcje unary (jednoargumentowe)
# znacznie uproszczenie kodu. pochodzi z rachunku lambda i testowania algorytmów.


def add(a, b):
    return a + b


def add_(a):
    def inner(b):
        return a + b

    return inner


add_five = add_(5)

result = add_five(42)

# print(result)


# one more


def multiply(x, y, z):
    return x * y * z


def multiply_(x):
    def wrapper(y):
        def inner(z):
            return x * y * z

        return inner

    return wrapper


multiply_by_two = multiply_(2)

print(multiply_by_two(10)(3))


# final example


def filter_list(predicate, lst):
    return [elem for elem in lst if predicate(elem)]


def is_even(x):
    return x % 2 == 0


filtering = filter_list(is_even, [1, 2, 3, 4, 5])
print(filtering)


def filter_list_(predicate):
    def inner(lst):
        return [elem for elem in lst if predicate(elem)]
    return inner


filtering_ = filter_list_(is_even)

print(filtering_([1, 2, 3, 4, 5]))

