"""cc4.py
Given a list of strings, group the anagrams together.
Order inside each group doesn't matter.
Order of groups doesn't matter.
"""
from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    res = []

    anagram_map = defaultdict(list)

    for word in words:
        key = tuple((sorted(word)))
        anagram_map[key].append(word)

    return list(anagram_map.values())
