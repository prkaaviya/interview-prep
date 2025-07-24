"""test_cc3.py"""
from cc3 import top_k_frequent


def test_top_k_frequent():
    result = top_k_frequent([
        "apple",
        "banana",
        "apple",
        "orange",
        "banana",
        "apple"
    ], 2)

    assert result == ["apple", "banana"]
