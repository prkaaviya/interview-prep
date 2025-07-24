"""test_cc5.py"""
from cc5 import longest_consecutive


def test_longest_consecutive():
    lst = [100, 4, 200, 1, 3, 2, 6, 7, 8]

    res = longest_consecutive(lst)

    # the longest sequence is [1, 2, 3, 4], and its length is 4
    assert res == 4
