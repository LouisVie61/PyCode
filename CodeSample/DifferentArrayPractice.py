# series of prefix_sum, different array, suffix_array implementation
def diffArray(nums: list, queries: list, k: int) -> bool:
    n = len(nums)
    diff = [0] * (n + 1)

    for i in range(k):
        li, ri, vali = queries[i]
        diff[li] -= vali
        diff[ri + 1] += vali # cancel effect after ri

    # update the segment of decrement
    # use prefix sum for updating purpose
    cur = 0
    for i in range(n):
        cur += nums[i]
        if cur + nums[i] > 0:
            return False

    return True