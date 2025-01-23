# I've got the problem when using 2D array with Dynamic Programming
# Instead of using the 2D, we can just only use 1D array


def findLargestProduct(nums):
    n = int(len(nums))
    dp = [[0] * n for _ in range(n)]
    for i in range(0, n - 1, 1):
        for j in range(i, n, 1):
            dp[i][j] = max(nums[i] * nums[j], nums[i] * dp[i + 1][j], nums[j] * dp[i][j - 1])
            if j == i:
                dp[i][j] = nums[i]


    maxProduct = -200
    for i in range (0, n, 1):
        for j in range(0, n, 1):
            if maxProduct < dp[i][j]:
                 maxProduct = dp[i][j]


    print(*dp)
    return maxProduct

arr = [2, 3, -2, 4]
print(findLargestProduct(arr))