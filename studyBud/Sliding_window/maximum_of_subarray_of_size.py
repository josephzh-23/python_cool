import sys

#find all anagrams

#calculate the max of each sum k in the array

arr = [100, 200, 300, 400]
k = 2

# Find the maximum sum here of a certain size

def maxSumOfSize(arr, n, k):

    maxSum = -sys.maxsize - 1
    for i in range(n -k + 1):
        curSum = 0
        for j in range(k):
            # meaning add the number starting from arr[i], this is quite important
            curSum = curSum + arr[i+ j]
        maxSum = max(curSum, maxSum)
    # update the results if resquired
    return maxSum


# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSumOfSize(arr, n, k))












