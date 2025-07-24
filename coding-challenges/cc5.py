"""cc5.py
Given an unsorted list of integers, return
the length of the longest consecutive
elements sequence. Algorithm must have O(n
time complexity.
"""


def longest_consecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num-1 not in num_set:
            current = num
            streak = 1
            while current+1 in num_set:
                current += 1
                streak += 1
            longest = max(longest, streak)

    return longest
