def countAndSay(n: int) -> str:
    def helper(s: str) -> str:
        res = ""
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                res += str(cnt) + s[i - 1]
                cnt = 1
        res += str(cnt) + s[-1]
        return res

    ans = "1"
    for _ in range(n - 1):
        ans = helper(ans)
    return ans

# Test
n1 = 4
expected = "1211"
print(countAndSay(n1))  # Output: "1211"
