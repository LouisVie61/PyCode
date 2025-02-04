def climbStairs(n: int) -> int:
    steps = [1, 2]
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(0, n + 1):
        for j in steps:
            if j <= i:
                dp[i] = dp[i] + dp[i - j]

    return dp[n]

n = int(input())
print(climbStairs(n))