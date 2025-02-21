import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from ProblemSolving.LeetCode203 import ListNode

from collections import deque
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append(new_path)

    return None

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B", "H"],
    "H": ["E"],
    "F": ["C"],
    "G": ["C"]
}

path = bfs(graph, "A", "H")
print(path)
