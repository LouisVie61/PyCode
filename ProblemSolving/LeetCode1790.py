def areAlmostEqual(s1: str, s2: str) -> bool:
    n = len(s1) # equal length as input said -> no need to check

    freq = [0] * 26
    for i in range(len(s1)):
        freq[ord(s1[i]) - ord('a')] += 1
        freq[ord(s2[i]) - ord('a')] -= 1

    for i in range(26):
        if freq[i] != 0:
            return False

    cntError = 0
    for i in range(n):
        if s1[i] != s2[i]:
            cntError += 1
        if cntError > 2:
            return False

    if cntError == 1:
        return False

    return True


s1 = input()
s2 = input()
if areAlmostEqual(s1, s2):
    print("YES")
else:
    print("NO")