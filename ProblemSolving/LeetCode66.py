from typing import List

def plusOne(digits: List[int]) -> List[int]:
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        total = digits[i] + carry
        carry = total // 10
        digits[i] = total % 10

    if carry > 0:
        digits.insert(0, carry)

    return digits