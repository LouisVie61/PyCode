# hard problem (advanced)
def findMin(nums):
    min = 5000
    for num in nums:
        if num < min:
            min = num

    return min

arr = [3,3,1,3]
print(findMin(arr))
arr2 = [1,1]
print(findMin(arr2))