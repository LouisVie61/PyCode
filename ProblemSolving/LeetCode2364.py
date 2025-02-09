import collections
from typing import List
import math


def cntBadPairs(nums: List[int]) -> int:
    cnt = 0
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (j - i) != (nums[j] - nums[i]):
                cnt += 1
    return cnt

def cntBadPairsWay2(nums: List[int]) -> int:
    n = len(nums)
    total_pairs = math.factorial(n) // (math.factorial(n - 2) * 2)
    my_map = {}
    for i in range(n):
        my_map[i] = nums[i] - i

    freq = [0] * (max(nums) + 1)
    for v in my_map.values():
        freq[v] += 1

    cntGoodPairs = 0
    for i in range(n):
        if freq[i] > 1:
            cntGoodPairs += (math.factorial(freq[i]) // (math.factorial(freq[i] - 2) * 2))

    return total_pairs - cntGoodPairs

arr = [4,1,3,3]
print(cntBadPairs(arr))
print(f'cach 2: {cntBadPairsWay2(arr)}')