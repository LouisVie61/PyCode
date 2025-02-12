from typing import List
# def check(n1, n2) -> bool:
#     sumD1 = 0
#     while n1:
#         sumD1 += n1 % 10
#         n1 //= 10
#
#     sumD2 = 0
#     while n2:
#         sumD2 += n2 % 10
#         n2 //= 10
#
#     return sumD1 == sumD2


# def maximumSumW1(nums: List[int]) -> int:
#     n = len(nums)
#     if n == 1:
#         return nums[0]
#
#     max_sum = 0
#     # brute force
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if check(nums[i], nums[j]):
#                 max_sum = max(max_sum, nums[i] + nums[j])
#
#     if max_sum == 0:
#         return -1
#     return max_sum


def maximumSumW2(nums: List[int]) -> int:
    n = len(nums)
    def getSumDigit(n1) -> int:
        sumD = 0
        while n1:
            sumD += n1%10
            n1 //= 10

        return sumD

    def maximumSumW1(lst: List[int]) -> int:
        if len(lst) < 2:
            return -1
        lst.sort(reverse=True)
        return lst[0] + lst[1]

    myMap = {}
    for i in range(n):
        key = getSumDigit(nums[i])
        if key in myMap:
            myMap[key].append(nums[i])
        else:
            myMap[key] = [nums[i]]

    maxSum = -1
    for val in myMap.values():
        if len(val) >= 2:
            maxSum = max(maxSum, maximumSumW1(val))

    return maxSum

nums1 = [18,43,36,13,7]
# print(f'Ket qua: {maximumSumW1(nums1)}')
print(f'Ket qua: {maximumSumW2(nums1)}')
nums2 = [10,12,19,14]
# print(f'Ket qua: {maximumSumW1(nums2)}')
