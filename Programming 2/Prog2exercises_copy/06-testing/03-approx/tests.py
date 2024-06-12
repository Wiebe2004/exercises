import pytest
from mystatistics import average


@pytest.mark.parametrize('ns, expected', [
    ([1], 1),
    ([1, 3], 2),
    ([5, 5, 5], 5),
    ([0.1, 0.1, 0.1], 0.1),
    ([3, 5, 4, 4, 4, 4], 4)
])
def test_average(ns, expected):
    assert pytest.approx(expected) == average(ns)