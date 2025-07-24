"""test_cc4.py"""
from cc4 import group_anagrams


def test_group_anagrams():
    lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
    match = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    result = group_anagrams(lst)

    assert result == match
