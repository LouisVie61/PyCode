def validNum(nums: list) -> str:
    n = len(nums[0])
    digit = ["0", "1"]
    # nums = ["01"]
    currentState = [""] * n
    frontier = []

    def genNum(index):
        if index == n:
            frontier.append("".join(currentState))
            return

        for i in range(len(digit)):
            currentState[index] = digit[i]
            genNum(index + 1)
            currentState[index] = ""
    genNum(0)

    for num in frontier:
        if num not in nums:
            return num

    return ""

nums = ["01"]
print(validNum(nums))

