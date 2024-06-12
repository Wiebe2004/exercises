from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert overlapping_intervals((4,9), (2, 10))
    assert not overlapping_intervals((1, 0), (5, 9))
    assert overlapping_intervals((2, 6), (3, 8))
    assert not overlapping_intervals((1, 2), (3, 4))
    assert overlapping_intervals((1, 3), (2, 4))
    assert not overlapping_intervals((0, 0), (1, 0))