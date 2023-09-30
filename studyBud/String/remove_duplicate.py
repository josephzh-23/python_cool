

#

# how to remove the duplicate here
# this allows you to remove the duplciate from python right here


nums = [1, 1, 2]
def removeDuplicates(nums):
    # this also worked as said before
    if len(nums) == 0:
        return 0

    l =1

    #for starter here
    for r in range(1, len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l+=1

    return l
    # and then here we have the code that we wanted here



removeDuplicates(nums)











