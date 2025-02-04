from typing import List

def findLongestSize(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return n

    maxLength = 0

    for i in range(n):
        for j in range(i, n):
            subArray = nums[i:j + 1]

            isAscending = True
            isDescending = True

            if len(subArray) <= 1:
                maxLength = max(maxLength, len(subArray))
                continue

            for k in range(1, len(subArray)):
                if subArray[k] > subArray[k - 1]:
                    isDescending = False
                elif subArray[k] < subArray[k - 1]:
                    isAscending = False
                else:
                    isAscending = False
                    isDescending = False

            if isAscending or isDescending:
                    maxLength = max(maxLength, len(subArray))

    return maxLength

arr = [3,3,3,3]
print(findLongestSize(arr))