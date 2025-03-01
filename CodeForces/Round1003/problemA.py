# Link Contests: https://codeforces.com/contest/2065

# Problem A

def convert(s: str) -> str:
    n = len(s)

    res = ""
    res += s[:n - 2]
    res += "i"

    return res

tc = int(input())
for t in range(tc, 0, -1):
    s = input()
    ans = convert(s)
    print(ans)

