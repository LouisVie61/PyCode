def rmOccurences(s: str, part: str) -> str:
    s = list(s)
    left = 0
    while left < len(s):
        right = left + len(part)

        if right > len(s):
            right = len(s)

        if (right - left) == len(part):
            if s[left:right] == list(part):
                del s[left:right]
                if left > len(part):
                    left -= len(part)

                if left > 0:
                    left -= 1
                continue
            else:
                left += 1
        else:
            left += 1

    return "".join(s)

# with the code above, I just deal with 20/80 test case.

def rmOccurences2(s: str, part: str) -> str:
    stack = []
    part_len = len(part)
    for char in s:
        stack.append(char)
        if len(stack) >= part_len and "".join(stack[-part_len:]) == part:
            del stack[-part_len:]

    return "".join(stack)

s = "daabcbaabcbc"
part = "abc"
print(rmOccurences(s, part))

print(rmOccurences2(s, part))