from typing import List


def queryResults(limit: int, queries: List[List[int]]) -> List[int]:
    hash_map = {}
    res = []
    for x, y in queries:
        hash_set = set()
        hash_map[x] = y
        for val in hash_map.values():
            if val != 0:
                hash_set.add(val)

        cnt = len(hash_set)
        res.append(cnt)

    return res

limit = 4
queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
expected_output = [1,2,2,3,4]
print(queryResults(limit, queries))

# due to the large constraints, the code still have 3 tests case that couldn't pass