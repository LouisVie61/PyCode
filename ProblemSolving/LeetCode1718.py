def constructDistancedSequence(n: int) -> list:
    res = [0] * (2 * n - 1)
    is_number_used = [False] * (n + 1)

    def find_lexi(index) -> bool:
        if index == len(res):
            return True

        if res[index] != 0:
            return find_lexi(index + 1)

        for num in range(n, 0, -1):
            if is_number_used[num]:
                continue

            if num == 1:
                res[index] = 1
                is_number_used[1] = True

                if find_lexi(index + 1):
                    return True

                res[index] = 0
                is_number_used[1] = False

            elif index + num < len(res) and res[index + num] == 0:
                res[index] = res[index + num] = num
                is_number_used[num] = True

                if find_lexi(index + 1):
                    return True

                res[index] = res[index + num] = 0
                is_number_used[num] = False

        return False

    find_lexi(0)
    return res


n = 3
ans = constructDistancedSequence(n)
print(*ans)