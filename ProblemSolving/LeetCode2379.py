def minReColor(blocks: str, k: int) -> int:
    res = []

    left = right = 0

    n = len(blocks)

    cnt_B = 0
    while right < n:
        cnt_B += 1 if blocks[right] == 'B' else 0

        if right - left + 1 == k:
            res.append(k - cnt_B)

            if blocks[left] == 'B':
                if cnt_B == k:
                    return 0
                cnt_B -= 1
            left += 1

        # if cnt_B == k:
        #     return 0

        right += 1

    return min(res)

blocks = "WBBWWBBWBW"
k = 7
print(minReColor(blocks, k))


blocks_1 = "WBWBBBW"
k = 2
print(minReColor(blocks_1, k))


