def minimumLength(s: str) -> int:
    s = list(s)
    # stack = []
    # index = 0
    n = len(s)
    #
    # while index < n - 1:
    #     if s[index] == s[index + 1]:
    #         if stack:
    #             s[index] = stack.pop()
    #         else:
    #             s.pop(index)
    #             n -= 1
    #             continue
    #
    #         s.pop(index + 1)
    #         n -= 1
    #         index = max(0, index - 1)
    #     else:
    #         stack.append(s[index])
    #         index = index + 1
    #
    # return len(s)
    # any letter can be performed if a couple exists
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            return 1

    return n


tc = int(input())
for _ in range(tc):
    s = input().strip()
    print(minimumLength(s))