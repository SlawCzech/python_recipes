def is_perfect_length(sequence):
    n = len(sequence)
    # wersja bitowa:
    return ((n + 1) & n == 0) and (n != 0)

    # wersja nieefektywna:
    # counter = 1
    #
    # while True:
    #     x = 2 ** counter
    #     if x == n + 1:
    #         return True
    #     if x > n + 1:
    #         return False
    #     counter += 1


# Perfect binary tree: (2 ** n) - 1

class LevelOrderIterator:
    def __init__(self, sequence):
        if not is_perfect_length(sequence):
            raise ValueError(f'Sequence of length {len(sequence)} does not represent a perfect binary tree.')
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration('No more elements.')

        result = self._sequence[self._index]
        self._index += 1
        return result


exp_tree = ['*', '+', '-', 'a', 'b', 'c', 'd']

iterator = LevelOrderIterator(exp_tree)


# print(list(iterator))


def left_child(index):
    return 2 * index + 1


def right_child(index):
    return 2 * index + 2


class PreOrderIterator:
    def __init__(self, sequence):
        if not is_perfect_length(sequence):
            raise ValueError(f'Sequence of length {len(sequence)} does not represent a perfect binary tree.')
        self._sequence = sequence
        self._stack = [0]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._stack) == 0:
            raise StopIteration

        index = self._stack.pop()
        result = self._sequence[index]

        right_child_index = right_child(index)

        if right_child_index < len(self._sequence):
            self._stack.append(right_child_index)

        left_child_index = left_child(index)
        if left_child_index < len(self._sequence):
            self._stack.append(left_child_index)

        return result


iterator = PreOrderIterator(exp_tree)


# print(list(iterator))


class InOrderIterator:
    def __init__(self, sequence):
        if not is_perfect_length(sequence):
            raise ValueError(f'Sequence of length {len(sequence)} does not represent a perfect binary tree.')
        self._sequence = sequence
        self._stack = []
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._stack) == 0 and self._index >= len(self._sequence):
            raise StopIteration

        while self._index < len(self._sequence):
            self._stack.append(self._index)
            self._index = left_child(self._index)

        index = self._stack.pop()
        result = self._sequence[index]
        self._index = right_child(index)

        return result


iterator = InOrderIterator(exp_tree)
# print(list(iterator))

# PostOrderIterator -> zadanie domowe!


missing = object()


class SkipMissingIterator:
    def __init__(self, iterable):
        self._iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self._iterator)
            if item is not missing:
                return item


exp_tree = ['+', 'r', '*', missing, missing, 'p', 'q']
iterator = SkipMissingIterator(InOrderIterator(exp_tree))
# print(list(iterator))


typesetting_table = {
    "-": "\u2212",
    "*": "\u00D7",
    "/": "\u00F7"
}


class TranslationIterator:
    def __init__(self, table, iterable):
        self._table = table
        self._iterator = iterable

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._iterator)
        return self._table.get(item, item)


exp_tree = ['-', 'r', '*', missing, missing, 'p', 'q']
iterator = TranslationIterator(typesetting_table, SkipMissingIterator(InOrderIterator(exp_tree)))
print(list(iterator))
