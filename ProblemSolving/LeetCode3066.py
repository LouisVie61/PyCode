from typing import List


def minOperation(nums: List[int], k: int) -> int:
    counting = 0
    import heapq
    heapq.heapify(nums)

    while nums[0] < k:
        x = heapq.heappop(nums)
        if not nums:
            break
        y = heapq.heappop(nums)
        new_element = x * 2 + y
        heapq.heappush(nums, new_element)
        counting = counting + 1

    return counting

nums = [2,11,10,1,3]
k = 10
print(minOperation(nums, k))

nums2 = [1,1,2,4,9]
j = 20
print(minOperation(nums2, j))
