from print_list import printList
from studyBud.Basics.binary_search import binarySearch

# find the first and last position of elem in sorted array
nums = [5, 7, 7, 8, 8, 10]

# and then continue here need to be done in O(log(n))


def findFirstAndLastElem(nums, target):
    left = findLeftOccurence(nums, target)
    right = findRightOccurence(nums, target)
    return [left, right]

def findLeftOccurence(nums, target):
    index = -1
    low = 0
    high = len(nums)

    while low <= high:
        mid =( low  + high)//2

        if(nums[mid] == target):
            index = mid
            high = mid - 1 # look in the right sub array
        elif (nums[mid] <target):
             low = mid + 1
        else:
            high = mid - 1

    return index


def findRightOccurence(nums, target):
    index = -1
    low = 0
    high = len(nums)

    while low <= high:
        mid = (low + high)//2

        if(nums[mid] == target):
            index = mid
            low = mid+  1 # look in the right subarray
        elif (nums[mid] < target):
            low = mid + 1
        else:
            high = mid - 1

    return index




print(findFirstAndLastElem(nums,7))











