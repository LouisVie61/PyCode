# one week later do
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 1:
        return strs[0]

    ans = ""
    strs.sort()
    first_str = strs[0]
    last_str = strs[-1]

    for i in range(min(len(first_str), len(last_str))):
        if first_str[i] != last_str[i]:
            return ans
        ans += first_str[i]

    return ans

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
