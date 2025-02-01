# I've got the problem when using 2D array with Dynamic Programming
# Instead of using the 2D, we can just use 1D array


def findLargestProduct(nums):
    n = len(nums)
    if n == 0:
        return 0

    max_fur = min_fur = nums[0]
    result = nums[0]

    for i in range(1, n):
        cur = nums[i]
        tmp_max = max(cur, max_fur * cur, min_fur * cur)
        min_fur = min(cur, max_fur * cur, min_fur * cur)
        max_fur = tmp_max
        result = max(result, max_fur)

    return result


arr = [-4, -3, -2]
print(findLargestProduct(arr))
