import pytest
from mystatistics import average


@pytest.mark.parametrize(
    "ns, expected",
    [
        ([5, 3, 7, 2], 4.25),
        ([3, 2, 1, 4], 2.5),
        ([0.1, 0.1, 0.1], 0.1),
    ],
)
def test_average(ns, expected):
    assert pytest.approx(expected) == average(ns)


# @pytest.mark.parametrize('ns',[
#     [5,3,7,2],
#     [3,2,1,4],
#     ([0.1, 0.1, 0.1], 0.1),
# ])
# def test_NOTaverage(ns):
#     actual = average(ns)
#     assert actual == False, f'{ns} is a good average'
