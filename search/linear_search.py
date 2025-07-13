""" linear search """
from typing import List


def linear_search(arr: List, target: int):
    for index, ele in enumerate(arr):
        if ele == target:
            return index
    return "Target not found"


num = 11
arr = [10, 3, 6, 4, 5, 2, 8, 0, 11, 9]
print(linear_search(arr, num))
