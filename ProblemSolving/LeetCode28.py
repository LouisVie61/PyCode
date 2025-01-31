def findFisrtOccurence(haystack, needle):
    answer = -1
    i = 0
    while i < len(haystack) - len(needle) + 1:
        if haystack[i] == needle[0]:
            ok = True
            suit_index = i
            for j in range(1, len(needle)):
                suit_index += 1
                if haystack[suit_index] != needle[j]:
                    ok = False
                    break

            if ok:
                answer = i
                break
        i += 1

    return answer


haystack = input()
needle = input()
print(findFisrtOccurence(haystack, needle))