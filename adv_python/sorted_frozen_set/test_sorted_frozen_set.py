import pytest
from .sorted_frozen_set import SortedFrozenSet


def test_construct_empty():
    SortedFrozenSet([])


def test_construct_from_not_empty_list():
    SortedFrozenSet([7, 8, 3, 1])


def test_construct_no_args():
    SortedFrozenSet()


def test_construct_from_iterator():
    items = [7, 8, 3, 1]
    iterator = iter(items)
    SortedFrozenSet(iterator)


# container_protocol ( in / not in) -


@pytest.fixture
def s():
    """return SortedFrozenSet object"""
    return SortedFrozenSet([6, 7, 3, 9])


def test_positive_contained(s):
    assert 7 in s


def test_negative_contained(s):
    assert not (10 in s)


def test_positive_not_contained(s):
    assert 10 not in s


def test_negative_not_contained(s):
    assert not (7 not in s)


# sized protocol - number of items; len(sized); `__len__`
# nie może zuzywać ani modyfikować kolekcji


def test_empty_with_default():
    s = SortedFrozenSet()
    assert len(s) == 0


def test_empty():
    s = SortedFrozenSet([])
    assert len(s) == 0


def test_one():
    s = SortedFrozenSet([42])
    assert len(s) == 1


def test_ten():
    s = SortedFrozenSet(range(10))
    assert len(s) == 10


def test_with_duplicates():
    s = SortedFrozenSet([5, 5, 5])
    assert len(s) == 1


# Iterable protocol
# `__iter__`  -> return iterator object
# alternatywa: `__getitem__`


@pytest.fixture
def s1():
    return SortedFrozenSet([7, 2, 1, 1, 9])


def test_iter(s1):
    iterator = iter(s1)
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 7
    assert next(iterator) == 9

    with pytest.raises(StopIteration) as ctx:
        next(iterator)
    assert "StopIteration()" in str(ctx)


def test_for_loop(s1):
    expected = [1, 2, 7, 9]
    index = 0
    for item in s1:
        assert item == expected[index]
        index += 1


# Sequence protocol  (indeksowanie lub slicing, index(val), count(val))
# musi być contained, sized and iterable!!
# przetwarza elementy po indeksie seq[index]
# opcjonalnie slicing se1[start:stop:step]
# reverse iterator
# znajdywanie elementów po wartości  sq.index(item)
# zlicza ilość konkretnych elementów sq.count(item)


@pytest.fixture
def s2():
    return SortedFrozenSet([1, 4, 9, 13, 15])


def test_index_zero(s2):
    assert s2[0] == 1


def test_index_last(s2):
    assert s2[-1] == 15


def test_index_three(s2):
    assert s2[3] == 13


def test_index_one_beyond_the_end(s2):
    with pytest.raises(IndexError) as ctx:
        s = s2[5]
    assert "IndexError('tuple index out of range')" in str(ctx)


def test_index_one_before_the_beginning(s2):
    with pytest.raises(IndexError) as ctx:
        s = s2[-6]
    assert "IndexError('tuple index out of range')" in str(ctx)


def test_slice_from_start(s2):
    assert s2[:3] == SortedFrozenSet([1, 4, 9])


def test_slice_to_end(s2):
    assert s2[3:] == SortedFrozenSet([13, 15])


def test_slice_empty(s2):
    assert s2[10:] == SortedFrozenSet()


def test_slice_arbitrary(s2):
    assert s2[2:4] == SortedFrozenSet([9, 13])


def test_slice_with_step(s2):
    assert s2[0:5:2] == SortedFrozenSet([1, 9, 15])


def test_slice_full(s2):
    assert s2[:] == s2


# Repr protocol
# `__repr__` -> str


def test_repr_empty():
    s = SortedFrozenSet()
    assert repr(s) == "SortedFrozenSet()"


def test_repr():
    s = SortedFrozenSet([42, 40, 19])
    assert repr(s) == "SortedFrozenSet([19, 40, 42])"


# Equality protocol


def test_positive_equal():
    assert SortedFrozenSet([4, 5, 6]) == SortedFrozenSet([6, 5, 4])


def test_negative_equal():
    assert not (SortedFrozenSet([4, 5, 6]) == SortedFrozenSet([1, 2, 3]))


def test_type_mismatch():
    assert not (SortedFrozenSet([1, 2, 3]) == [4, 5, 6])


def test_identical():
    s = SortedFrozenSet([1, 2, 3])
    assert s == s


# Inequality protocol


def test_positive_unequal():
    assert SortedFrozenSet([4, 5, 6]) != SortedFrozenSet([1, 2, 3])


def test_negative_unequal():
    assert not (SortedFrozenSet([4, 5, 6]) != SortedFrozenSet([6, 5, 4]))


def test_type_mismatch_unequal():
    assert SortedFrozenSet([1, 2, 3]) != [4, 5, 6]


def test_identical_unequal():
    s = SortedFrozenSet([1, 2, 3])
    assert not (s != s)


# Hashable protocol
# `__hash__`  -> integer hash code  (hash(obj))
# disable hash: __hash__ = None


def test_equal_sets_have_the_same_hash_code():
    assert hash(SortedFrozenSet([5, 2, 1, 4])) == hash(SortedFrozenSet([5, 2, 1, 4]))

