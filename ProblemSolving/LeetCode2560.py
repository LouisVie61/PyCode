def minCapability(nums: list, k: int) -> int:
    l, r = min(nums), max(nums)

    # greedy check capability for rob -> can get the valid (<=) his/her capability (stands for mid)
    def checkCapability(capability: int) -> bool:
        count, i = 0, 0
        while i < len(nums):
            if nums[i] <= capability:
                count += 1
                i += 1 # we ignore the continuous element when found the valid capability
            i += 1

        return count >= k

    while l < r:
        m = (l + r) // 2
        if checkCapability(m): # our goal is find the minimum capability
            r = m
        else:
            l = m + 1

    return l