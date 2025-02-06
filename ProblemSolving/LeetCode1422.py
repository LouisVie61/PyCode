def maxScore(s: str) -> int:
    n = len(s)
    score = 0

    totalOnes = 0
    for i in range(n):
        if s[i] == '1':
            totalOnes += 1

    cntZeros = 0
    cntOnes = 0
    for i in range(n - 1):
        if s[i] == '0':
            cntZeros += 1
        else:
            cntOnes += 1
        goal = cntZeros + (totalOnes - cntOnes)
        if score < goal:
            score = goal

    return score


s = input()
print(maxScore(s))