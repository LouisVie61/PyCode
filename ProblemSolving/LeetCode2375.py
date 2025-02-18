def smallestNumber(pattern: str) -> str:
    pattern = list(pattern)
    n = len(pattern)
    num = [0] * (n + 1)
    is_number_used = [False] * 10

    def gen_num(pos) -> bool:
        if pos == n + 1:
            return True

        for i in range(1, 10):
            if is_number_used[i]:
                continue

            if pos > 0:
                if pattern[pos - 1] == "I" and i < num[pos - 1]:
                    continue
                if pattern[pos - 1] == "D" and i > num[pos - 1]:
                    continue

            num[pos] = i
            is_number_used[i] = True

            if gen_num(pos + 1):
                return True

            # backtrack
            num[pos] = 0
            is_number_used[i] = False

        return False

    gen_num(0)

    return "".join(map(str, num))


# we can use monotonic stack to solve the problem with higher efficiency
def alternativeWay(pattern: str) -> str:
    stack = []
    result = []

    for i in range(len(pattern) + 1):
        stack.append(str(i + 1))

        if i == len(pattern) or pattern[i] == "I":
            while stack:
                result.append(stack.pop())

    return "".join(result)

pattern_1 = "II"
pattern_2 = "ID"
pattern_3_example = "IIIDIDDD"
pattern_4_example = "DDD"

print(f'Ket qua 1: {smallestNumber(pattern_1)}')
print(f'Ket qua 2: {alternativeWay(pattern_2)}')
print(f'Ket qua 2: {smallestNumber(pattern_2)}')
print(f'Ket qua 3: {smallestNumber(pattern_3_example)}')
print(f'Ket qua 4: {smallestNumber(pattern_4_example)}')
