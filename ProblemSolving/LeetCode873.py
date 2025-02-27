from collections import defaultdict


def lenLongestSubsequence(arr: list) -> int:
    index = {val: i for i, val in enumerate(arr)}
    dp = defaultdict(lambda: 2) # create a default dictionary with the default length is two.
    max_length = 0

    for k in range(len(arr)):
        for j in range(k):
            i = index.get(arr[k] - arr[j]) # fast lookup.

            if i is not None and i < j:
                dp[(j, k)] = dp[(i, j)] + 1
                if dp[(j, k)] >= 3:
                    max_length = max(max_length, dp[(j, k)])

    return max_length if max_length >= 3 else 0