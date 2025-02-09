from typing import List


def cntBadPairs(nums: List[int]) -> int:
    cnt = 0
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (j - i) != (nums[j] - nums[i]):
                cnt += 1
    return cnt

arr = [1,2,3,4,5]
print(cntBadPairs(arr))