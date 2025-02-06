from typing import List

vowelList = {'u', 'a', 'i', 'o', 'e'}

def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    res = []
    for query in queries:
        cnt = 0
        for i in range(query[0], query[1] + 1):
            n = len(words[i])
            if words[i][0] in vowelList and words[i][n - 1] in vowelList:
                cnt += 1
        res.append(cnt)

    return res

# the first way using nested loops to deal with assignment => over the large constraints => TLE O(n^2)
# the second way using prefix_sum and knowledge of counting sum in subarray => O(n)

def way2(words: List[str], queries: List[List[int]]) -> List[int]:
    res = []
    n = len(words)
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        ok = words[i][0] in vowelList and words[i][-1] in vowelList
        prefix_sum[i + 1] = prefix_sum[i] + ok # true = 1, false = 0

    for l, r in queries:
        cnt = prefix_sum[r + 1] - prefix_sum[l]
        res.append(cnt)

    return res


words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
res = vowelStrings(words, queries)
print(res)