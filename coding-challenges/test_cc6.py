"""test_cc6.py"""
from cc6 import two_sum


def test_two_sum():
    nums = [2, 7, 11, 15]
    target = 13

    res = two_sum(nums, target)

    assert res == [0, 2]
