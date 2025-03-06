def findSth(grid: list) -> list:
    visited = [] * ((len(grid) * len(grid[0])) + 1)
    duplicateNum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in visited:
                duplicateNum = grid[i][j]
            visited.append(grid[i][j])

    visited.sort()
    if min(visited) > 1:
        return [duplicateNum, 1]

    missingNum = 0
    for i in range(len(visited) - 1):
        if visited[i + 1] - visited[i] > 1:
            missingNum = visited[i] + 1
            break

    if missingNum == 0:
        missingNum = visited[-1] + 1

    return [duplicateNum, missingNum]


def alternativeCode(grid: list) -> list:
    seen = {}
    n = len(grid)
    curSum = ((n*n) * ((n*n) + 1)) // 2
    dup = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] not in seen:
                curSum -= grid[i][j]
                seen[grid[i][j]] = 1
            else:
                dup = grid[i][j]

    return [dup, curSum]

grid_1 = [[1,3],[2,2]]
grid_2 = [[9,1,7],[8,9,2],[3,4,6]]
list1 = findSth(grid_1)
list2 = findSth(grid_2)

break_tc = [[2,2],[3,4]]
list3 = findSth(break_tc)
# expected output: [2,1]

list4 = alternativeCode(break_tc)

print(list1)
print(list2)
print(list3)
print(list4)