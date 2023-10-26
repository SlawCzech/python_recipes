import sys
from bisect import bisect_left
from collections.abc import Set, Sequence
from itertools import chain


class SortedFrozenSet(Sequence, Set):
    def __init__(self, items=None):
        self._items = tuple(sorted(set(items) if items is not None else set()))

    def __contains__(self, item):
        return item in self._items
        # return self._items.__contains__(item)  # tak nie rób, bo to low level api

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        # return iter(self._items)
        for item in self._items:
            yield item

    def __getitem__(self, index):
        result = self._items[index]
        return (
            SortedFrozenSet(result)
            if isinstance(index, slice)
            else result
        )

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._items == other._items

    def __repr__(self):
        args = repr(list(self._items)) if self._items else ""
        return f'{type(self).__name__}({args})'

    def __hash__(self):
        return hash((type(self), self._items))

    def __add__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return SortedFrozenSet(chain(self._items, other._items))

    def __mul__(self, other):
        if not isinstance(other, int):
            return TypeError(f'Cannot multiply sequence by non-int type {type(other)}')
        return self if other > 0 else SortedFrozenSet()

    def __rmod__(self, other):
        return self * other

    def index(self, item, start=0, stop=sys.maxsize):
        idx = bisect_left(self._items, item, lo=start, hi=stop)
        if (idx != len(self._items)) and self._items[idx] == item:
            return idx
        raise ValueError(f'{item!r} not found.')

        # for idx, elem in enumerate(self._items):
        #     if elem == item:
        #         return idx
        #     idx += 1
        #
        # raise ValueError(f'{item!r} not found.')

    def count(self, item):
        return int(item in self)

    def issubset(self, iterable):
        return self <= SortedFrozenSet(iterable)

    def issuperset(self, iterable):
        return self >= SortedFrozenSet(iterable)

    def intersection(self, iterable):
        return self & SortedFrozenSet(iterable)

    def symmetric_difference(self, iterable):
        return self ^ SortedFrozenSet(iterable)

    def union(self, iterable):
        return self | SortedFrozenSet(iterable)

    def difference(self, iterable):
        return self - SortedFrozenSet(iterable)
