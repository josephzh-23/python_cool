from print_list import printList


resList = []
def permute(nums):
    backtrack([], nums)
    print(resList)



def backtrack(tempList, nums):

    # baes case
    if(len(tempList) == len(nums)):
        resList.append(tempList.copy())
        print("final list is ", resList)
        return

    for num in nums:

        # skip if we get the same element here
        if(num in tempList):
            continue


        # if not already contains then we add it rigth here
        tempList.append(num)

        # go back to try other elements
        backtrack(tempList, nums)

        # this will be called since we ar ein a lok for 3 times
        tempList.pop()


permute([1, 2, 3])






