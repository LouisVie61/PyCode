def numTitlePossibilities(titles: str) -> int:
    visited = set()

    def gen_title(word, used):
        if word:
            visited.add("".join(word))

        for i in range(len(titles)):
            if used[i]:
                continue

            if i > 0 and titles[i] == titles[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            word.append(titles[i])

            gen_title(word, used)

            used[i] = False
            word.pop()

    titles = "".join(sorted(titles))
    gen_title([], [False] * len(titles))
    return len(visited)

s = "AAB"
print(numTitlePossibilities(s))
