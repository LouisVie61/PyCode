from typing import List
from LeetCode203 import ListNode

def tupleSameProduct(nums: List[int]) -> int:
    n = len(nums)
    nums.sort()

    pairs = {}
    for i in range(n):
        for j in range(i + 1, n):
            product = nums[i] * nums[j]
            if product not in pairs:
                pairs[product] = [(nums[i], nums[j])]
            else:
                pairs[product].append((nums[i], nums[j]))

    cnt = 0
    for key, value in pairs.items():
        num_pairs = len(value)
        if num_pairs >= 2:
            cnt += (num_pairs * (num_pairs - 1) // 2) * 8
            # // 2 because counting 2 times of 1 [pairs + pairs]

    return cnt


arr = [1,2,4,5,10]
print(tupleSameProduct(arr))