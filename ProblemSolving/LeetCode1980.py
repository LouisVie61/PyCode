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

def alternativeWay(nums: list) -> str:
    n = len(nums[0])
    num_set = set(nums)  # Use a set for O(1) lookup

    def generate_binary(curr):
        if len(curr) == n:  # Base case: if we have built an n-length string
            if curr not in num_set:  # If it's not in the given list, return it
                return curr
            return None

        # Try adding '0' and '1' to build a new string
        result = generate_binary(curr + '0')
        if result:  # If we found a valid missing string, return it
            return result
        return generate_binary(curr + '1')

    return generate_binary("")


# instead of storing and generating all combinations, we can only store and generate a valid option
# the alternative way is represented by the second function with recursion

nums = ["01"]
print(validNum(nums))

