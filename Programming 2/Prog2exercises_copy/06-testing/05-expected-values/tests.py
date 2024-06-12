import pytest
import itertools
from mergesort import split_in_two

@pytest.mark.parametrize('ns', [list(range(n)) for n in range(101)])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert left + right == ns, "Left & right halves do not recombine to original list."
    assert abs(len(left) - len(right)) <= 1, "Left & right halves' lengths differ by more than 1"




@pytest.mark.parametrize('left', [
    [],
    [1],
    [2, 3],
    [54, 23, 10, 10, 4],
    [2, 1, 2],
    [3, 0, 0, 3]
])
@pytest.mark.parametrize('right', [
    [],
    [2],
    [4, 5],
    [20, 12, 12, 4],
    [4, 6, 69, 2],
    [2, 4, 5, 20]
])
def test_merge_sorted(left, right):
    assert test_merge_sorted(left, right) == sorted(left + right)



@pytest.mark.parametrize('ns', 'expected', [
    ([1, 0, 53, 6], [0, 1, 6, 53]),
    ([5, 3, 42, 0], [0, 3, 5, 42]),
    ([4, 2, 9, 4], [2, 4, 4, 9]),
    ([20, 3, 1, 24], [1, 3, 20, 24]),
    ([6, 3, 7, 3], [3, 3, 6, 7]),
])
def test_merge_sort(expected, ns):
    assert itertools.permutations(ns) == expected