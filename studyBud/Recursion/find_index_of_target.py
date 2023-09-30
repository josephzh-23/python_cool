


list = [2,3, 1, 4, 4,5]

def findIndex(arr, target, index):
    if index == len(arr):
        return -1

    if arr[index] == target:
        return index
    else:
        return findIndex(arr, target, index+1)
print(findIndex(list, 7, 0))