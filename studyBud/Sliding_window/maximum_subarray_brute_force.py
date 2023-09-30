import math
import sys
from typing import List


# n is the size here
def maxSubArray(nums: List[int]) -> int:
    max_subarray = -math.inf
    for i in range(len(nums)):
        current_subarray = 0
        for j in range(i, len(nums)):
            print(current_subarray)
            current_subarray += nums[j]
            max_subarray = max(max_subarray, current_subarray)

    return max_subarray

maxSubArray([4, -1, 2, 1])




