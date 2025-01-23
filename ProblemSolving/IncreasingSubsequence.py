def ascendingSubsequence(arr, n):
    tails = []

    for num in arr:
        # not tails: means: is empty or not
        if not tails or num > tails[-1]:
            tails.append(num)
        else:
            l , r = 0, len(tails) - 1
            while l <= r:
                m = (l + r) // 2
                if tails[m] < num:
                    l = m + 1
                else:
                    r = m - 1
            tails[l] = num

    return len(tails)


n = int(input())
arr = list(map(int, input().split()))
print(ascendingSubsequence(arr, n))