# Ex1: Input: days = 10, meetings = [[5,7],[1,5],[9,10]]
# Output: 1 // miss 8th
# 1 <= days <= 10^9
# 3 5 2 overlapping: 5th
# 10 - (3 + 5 + 2 - 1) = 1

# Ex2: Input: days = 5, meetings = [[2,4],[1,3]]
# sort start[ith] in ascending order => [[1,3],[2,4]]
# merge: ending[prev] >= start[next] -> [start[prev],end[next]] -> [1,4] -> adjacent = 4 => 5 - 4 = 1
# Output: 1

def sorting(meetings):
    return sorted(meetings, key=lambda meeting: meeting[0])

def merge(meetings) -> list:
    meetings = sorting(meetings)
    res = [meetings[0]]

    for i in range(1, len(meetings)):
        last = res[-1]
        if last[1] >= meetings[i][0]:
            last[1] = max(last[1], meetings[i][1])
        else:
            res.append(meetings[i])

    return res

def calculateAdjacent(meetings) -> int:
    n = len(meetings)
    total = 0

    for i in range(n):
        total += (meetings[i][1] - meetings[i][0] + 1)

    return total

def countDays(days, meetings) -> int:
    handled = merge(meetings)
    workMeet = calculateAdjacent(handled)
    return days - workMeet

arr_1 = [[5,7],[1,3],[9,10]]
days_1 = 10
print(f'result 1:{countDays(days_1, arr_1)}')
#expected = 2

arr_2 = [[2,4],[1,3]]
days_2 = 5
print(f'result 2:{countDays(days_2, arr_2)}')

arr_3 = [[1,6]]
days_3 = 6
print(f'result 3:{countDays(days_3, arr_3)}')