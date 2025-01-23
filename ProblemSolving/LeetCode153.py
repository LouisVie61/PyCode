def findMin(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


arr = [1,2,3,4,5]
print(f'Ket qua 1: {findMin(arr)}')
arr2 = [4,5,6,7,0,1,2]
print(f'Ket qua 2: {findMin(arr2)}')