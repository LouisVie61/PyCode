def closestPrime(left: int, right: int) -> list:
    ans = []
    def genPrimes(leftPoint: int, rightPoint: int) -> list:
        prime = [True for index in range(rightPoint + 1)]
        p = 2
        res = []
        while p * p <= rightPoint:
            if prime[p]:

                for i in range(p * p, rightPoint + 1, p):
                    prime[i] = False
            p += 1

        for p in range(2, rightPoint + 1):
            if prime[p] and p >= leftPoint:
                res.append(p)

        return res

    ans = genPrimes(left, right)

    if len(ans) <= 1:
        return [-1, -1]

    ans.sort()

    resTable = {}

    minimumDis = 10 ** 6

    for i in range(len(ans) - 1):
        tmp = ans[i:i + 2]
        distance = abs(tmp[0] - tmp[1])

        if distance not in resTable:
            resTable[distance] = []
        resTable[distance].append(tmp)

        minimumDis = min(minimumDis, distance)

    if minimumDis in resTable:
        return resTable[minimumDis][0]

    return [-1, -1]


left = 10
right = 19
expected = [11, 13]
print(closestPrime(left, right))


