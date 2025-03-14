def maximumCandies (candies: list, k: int) -> int:
    if sum(candies) < k:
        return 0

    # check the number of candy for each child is m, whether we have enough candies for all children?
    # cach hoat dong
    # chia tung dong keo cho m, tinh tong so phan keo co the tao ra
    # new tong so phan keo (cnt) >= so tre (k), nghia la co the chia it nhat k phan -> hop le
    def check(m):
        cnt = sum(c // m for c in candies)
        return cnt >= k

    l, r = 1, max(candies)
    while l < r:
        mid = (r + l + 1) // 2
        if check(mid):
            l = mid
        else:
            r = mid - 1

    return l


arr = [4,7,5]
k = 4
print(maximumCandies(arr, k))