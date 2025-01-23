# the first way is dynamic programming with nested loops
# because the nested loops would upto n^2 in time complexity.
# In contrast, the constraint of the assignment is upto 2 * 10^5 for the length
# of an array could have.
# the second way, after asking for Gemini => use tail array and search for other numbers
# which is suitable for the assignment.


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