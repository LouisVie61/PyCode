from typing import List


def maximumAscending(nums: List[int]) -> int:
    n = len(nums)

    if n < 1:
        return 0
    if n == 1:
        return nums[0]

    maxVal = 0

    for i in range(n):
        for j in range(i, n):
            sub_array = nums[i:j + 1]
            if not sub_array:
                continue

            isAscending = True
            for k in range(1, len(sub_array)):
                if sub_array[k - 1] >= sub_array[k]: # fix here
                    isAscending = False
                    break

            if isAscending:
                maxVal = max(maxVal, sum(sub_array))

    return maxVal

def newWayToSolve(nums: List[int]) -> int:
    n = len(nums)
    if n < 1:
        return 0

    maxTotal = nums[0]
    curTotal = nums[0]

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            curTotal += nums[i]
        else:
            curTotal = nums[i]

        maxTotal = max(maxTotal, curTotal)

    return maxTotal

arr = [3,6,10,1,8,9,9,8,9]
expected_output = 19
print(f'real_output way 1: {maximumAscending(arr)}')
print(f'real_output way 2: {newWayToSolve(arr)}')