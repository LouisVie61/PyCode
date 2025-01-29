def removeDuplicates(nums):
    k = 1
    left = 0
    right = 1
    while right < len(nums):
        if nums[left] == nums[right]:
            nums[right] = '_'
        else:
            left += 1
            k += 1
            nums[left] = nums[right]
        right += 1
    print(*nums)
    return k

arr = [1,1,2]
print(removeDuplicates(arr))
