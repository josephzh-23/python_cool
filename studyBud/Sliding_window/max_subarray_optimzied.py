

# Any time we get a negative prefix we then remove it in this scenario here using this

def maxSubArray(nums):
    maxSub = nums[0]

    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
            # reset the toal up here
        curSum += n
        maxSum = max(maxSub, curSum)
    return maxSum












