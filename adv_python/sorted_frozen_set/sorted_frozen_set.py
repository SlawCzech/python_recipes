class SortedFrozenSet:
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
