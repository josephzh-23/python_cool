

# convert the number to string

# find the solution here

# take in a list of numbers here

# the approach ehre: extract digits from an integer and only stop
# when our digit reaches 0 as said
def findNumbers(nums):

    totalCountEvent = 0

    for i in range (len(nums)):
        count1 = 0

        while nums[i] > 0:
            nums[i] = nums[i] // 10
            count1+=1
        if count1%2 ==0:
            totalCountEvent+=1

    return totalCountEvent



# an even number of digits here
nums = [12, 345, 2, 6, 7896]
#check for the odd number of digits here

print("the number is ", findNumbers(nums))