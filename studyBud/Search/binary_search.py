from typing import List

from studyBud.Basics.binary_search import binarySearch


def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1

    # so if the array is [4, 5, 6, 7, 0, 1, 2],
    # then the index of the pivot element would be 0
    # Find the index of the pivot element (the smallest element)
    while left <= right:


        # this floor division rounds down here
        mid = (left + right) // 2
        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid - 1


    # Binary search over elements on the pivot element's left
    if (answer := binarySearch(nums, 0, left - 1, target)) != -1:
        return answer

        # Binary search over elements on the pivot element's right
    return binarySearch(nums, left, n - 1, target)