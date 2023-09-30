# Binary search over an inclusive range [left_boundary ~ right_boundary]
def binarySearch(nums, left_boundary, right_boundary, target):
    left, right = left_boundary, right_boundary
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [1, 2, 3, 4, 5]
len(arr) # this will actually give 4 different from array.size in kotlin
print(binarySearch(arr, 0, len(arr), 5))