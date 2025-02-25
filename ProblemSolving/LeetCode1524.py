def numOfSubarrays(arr: list) -> int:
    n = len(arr)
    mod = 10 ** 9 + 7
    prefix = 0
    even_count = 1
    odd_count = 0

    ans = 0
    for i in range(n):
        prefix += arr[i]
        if prefix%2 == 0:
            even_count += 1
            ans += odd_count
        else:
            odd_count += 1
            ans += even_count

        ans %= mod

    return ans

def dynamicProgramming(arr: list) -> int:
    mod = 10 ** 9 + 7
    n = len(arr)

    dp_even, dp_odd = [0] * n, [0] * n

    for i in range(n):
        arr[i] %= 2

    if arr[n - 1] == 0:
        dp_even[n - 1] = 1
    else:
        dp_even[n - 1] = 1

    for num in range(n - 2, -1, -1):
        if arr[num] == 0:
            dp_even[num] = (1 + dp_even[num + 1]) % mod
            dp_odd[num] = dp_odd[num + 1]
        else:
            dp_odd[num] = (1 + dp_odd[num + 1]) % mod
            dp_even[num] = dp_odd[num + 1]

    cnt = 0
    for i in range(len(dp_odd)):
        cnt += dp_odd[i]
        cnt %= mod

    return cnt

arr = [2,4,6]
print(numOfSubarrays(arr))

arr2 = [2, 4, 6]
print(dynamicProgramming(arr2))