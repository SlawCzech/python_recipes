# map filter reduce => paradygmat funkcyjny, gdyż
# higher order functions, pure functions, lazy evaluated

# def my_map(arr):
#     result = []
#     for elem in arr:
#         result.append(elem * 2)
#     return result


# print(my_map([1, 2, 3, 4]))


def my_map(cb, collection):
    for item in collection:
        yield cb(item)


print(my_map(lambda x: x * 2, [1, 2, 3, 4]))


def my_filter(cb, collection):
    for item in collection:
        if cb(item):
            yield cb(item)


print(list(my_filter(lambda x: x / 2 > x // 2, [1, 2, 3, 4])))


def my_reduce(cb, collection, start=None):
    accumulator = collection[0] if start is None else start

    for item in collection[1 if start is None else 0:]:
        accumulator = cb(accumulator, item)

    return accumulator


print(my_reduce(lambda acc, ce: acc + ce, [1, 2, 3, 4], 0))

