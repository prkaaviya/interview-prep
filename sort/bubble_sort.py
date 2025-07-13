""" bubble sort"""
from typing import List


def bubble_sort(arr: List) -> List:
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [3, 17, 2, 15, 21, 5, 11, 4, 8, 6]
print(bubble_sort(arr))
