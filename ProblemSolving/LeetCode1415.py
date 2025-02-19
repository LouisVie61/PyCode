def getHappyString(n: int, k: int) -> str:
    frontier = [] # store (a copy) valid string
    currentState = [""] * n # valid string
    components = ["a", "b", "c"]

    def helper(index):
        if index == n:
            frontier.append("".join(currentState))
            return

        for i in range(len(components)):
            if index > 0 and currentState[index - 1] == components[i]:
                    continue

            currentState[index] = components[i]
            helper(index + 1)
            #backtrack
            currentState[index] = ""


    helper(0)
    return frontier[k - 1] if k <= len(frontier) else ""

n = 1
k = 3
print(getHappyString(n, k))

# at the problem I was made a big mistake
# I returned (t or f) too early, that can only make a valid happy string
# whereas, the problem requires generate all combinations as possible.
# Note.