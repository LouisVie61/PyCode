def applyOperations(nums: list) -> list:
    n = len(nums)
    res = [0] * n
    count = 0
    i = 0

    while i < n - 1:
        if nums[i] != 0:
            if nums[i] == nums[i + 1]:
                res[count] = nums[i] * 2
                i += 1
            else:
                res[count] = nums[i]
            count += 1
        i += 1

    if i < len(nums) and nums[i] != 0:
        res[count] = nums[i]

    return res

arr = [1,2,2,1,1,0]
print(applyOperations(arr))
# arr2 = [0,1]
# print(applyOperations(arr2))

