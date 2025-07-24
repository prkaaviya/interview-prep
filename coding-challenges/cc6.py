"""cc6.py
Given a list of integers and a target, return
the indices of the two numbers that add up to
the target. Each input has exactly one solution,
and same element cannot be used twice.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    index_map = {}

    for index, num in enumerate(nums):
        complement = target - num
        if complement in index_map:
            return [index_map[complement], index]
        index_map[num] = index
