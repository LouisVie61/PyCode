def smallestNumber(pattern: str) -> str:
    pattern = list(pattern)
    n = len(pattern)
    num = [0] * (n + 1)
    is_number_used = [False] * 9

    def gen_num(pos) -> bool:
        if pos == n + 1:
            return True

        if num[pos] != 0:
            return gen_num(pos + 1)

        for i in range(1, 10):
            if is_number_used[i - 1]:
                continue

            num[pos] = i
            is_number_used[i - 1] = True

            if gen_num(pos):
                return True

            # back_track
            num[pos] = 0
            is_number_used[i - 1] = False

        return False

    gen_num(0)

    return "".join(map(str, num))


pattern_1 = "II"
pattern_2 = "ID"
pattern_3_example = "IIIDIDDD"
pattern_4_example = "DDD"

print(f'Ket qua 1: {smallestNumber(pattern_1)}')
print(f'Ket qua 2: {smallestNumber(pattern_2)}')
print(f'Ket qua 3: {smallestNumber(pattern_3_example)}')
print(f'Ket qua 4: {smallestNumber(pattern_4_example)}')
