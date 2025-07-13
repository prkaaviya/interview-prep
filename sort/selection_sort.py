""" selection sort """
from typing import List


def selection_sort(arr: List) -> List:
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [3, 17, 2, 15, 21, 5, 11, 4, 8, 6]
print(selection_sort(arr))
