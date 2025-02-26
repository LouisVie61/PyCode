# kadane's algorithm
def maxAbsSubarray(nums: list) -> int:
    if len(nums) <= 1:
        return abs(nums[0])

    res = nums[0]
    minSum = maxSum = nums[0]

    for i in range(1, len(nums)):
        tmp = max(nums[i], maxSum + nums[i], minSum + nums[i])
        minSum = min(nums[i], minSum + nums[i], minSum + nums[i])
        maxSum = tmp
        res = max(res, abs(maxSum), abs(minSum))

    return res

# prefix sum implementation
def alternativeWay(nums: list) -> list:
    minCur, minSum, maxCur, maxSum = 0, 0, 0, 0
    for num in nums:
        maxSum, maxCur = max(maxSum, maxCur + num), max(maxCur + num, 0)
        minSum, minCur = min(minSum, minCur + num), min(minCur + num, 0)

    return max(maxSum, -minSum)

# related to the LeetCode152 problem
# kadane's algorithm: calculate the subarray sum min-N-max at the current index


nums_1 = [1,-3,2,3,-4] # expected output = 5
nums_2 = [2,-5,1,-4,3,-2] # expected output = 8
print(maxAbsSubarray(nums_1))
print(maxAbsSubarray(nums_2))
print(alternativeWay(nums_1))
print(alternativeWay(nums_2))
