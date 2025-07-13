""" binary search """
from typing import List


def binary_search(arr: List, target: int):
    left, right = 0, len(arr)-1 # len(arr) will give index out of bounds error

    while left <= right:
        mid = ( left + right ) // 2
        if target == arr[mid]:
            return True, arr[mid]
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return False


target = 66
# pos  0. 1. 2. 3. 4. 5. 6.  7.  8.  9.
arr = [2, 4, 5, 6, 7, 8, 10, 11, 19, 29]
print(binary_search(arr, target))