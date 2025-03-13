# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].
#
# Each queries[i] represents the following action on nums:
#
# Decrement the value at each index in the range [li, ri] in nums by at most vali.
# The amount by which each value is decremented can be chosen independently for each index.

# A Zero Array is an array with all its elements equal to 0.
#
# Return the minimum possible non-negative value of k,
# such that after processing the first k queries in sequence, nums becomes a Zero Array.
# If no such k exists, return -1.

# Constraints:
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 5 * 10^5
# 1 <= queries.length <= 10^5
# queries[i].length == 3
# 0 <= li <= ri < nums.length
# 1 <= vali <= 5

# use diff[] (mang chenh lech) for finding the valid with k
# use binary search for finding the first k queries - minimum

def minZeroArray(nums: list, queries: list) -> int:

    n = len(nums)
    q = len(queries)

    def canBeZeroArr(k):
        diff = [0] * (n + 1)

        for i in range(k):
            li, ri, vali = queries[i]
            diff[li] -= vali # start to decrement
            diff[ri + 1] += vali # cancel effect

        # Recover here
        cur_decre = 0
        for i in range(n):
            cur_decre += diff[i] # apply the effect
            if nums[i] + cur_decre > 0: # if nums[i] is still > 0 -> return False
                return False

        return True

    low, high = 0, q
    while low < high:
        mid = (low + high) // 2
        if canBeZeroArr(mid): # check if applying the first "mid" queries
            high = mid # if valid -> try the smaller "mid"
        else:
            low = mid + 1 # vice versa

    return low if canBeZeroArr(low) else -1
