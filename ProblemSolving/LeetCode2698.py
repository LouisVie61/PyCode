def find_partition(n: int) -> bool:
    squared = n ** 2

    s = str(squared)
    n_digits = len(s)

    def gen_partition(index, current_sum):
        if index == n_digits:
            return current_sum == n

        for i in range(index, n_digits):
            num = int(s[index:i + 1])
            print(f'lan: {i} va {s[index:i+1]} va {num} va {current_sum}')
            if num > n:
                break
            if gen_partition(i + 1, current_sum + num):
                return True
        return False

    return gen_partition(0, 0)


def punishmentNumber(n: int) -> int:
    ans = 0
    for i in range(1, n + 1):
        if find_partition(i):
            ans += i ** 2
    return ans

# n = 37
# # expected 182
# print(punishmentNumber(n))

print(find_partition(36))

# the problem seem hard because I am not tend to practice with this kind of problem before