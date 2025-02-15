class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def depth_limited_search(self, node, goal, depth_limit):
        if node == goal:
            return [node]
        if depth_limit <= 0:
            return None
        if node not in self.graph:
            return None

        for neighbor in self.graph[node]:
            path = self.depth_limited_search(neighbor, goal, depth_limit - 1)
            if path:
                return [node] + path
        return None

    def iterative_deepening_dfs(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            path = self.depth_limited_search(start, goal, depth)
            if path:
                return path
        return None


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

start_node = 0
goal_node = 6
max_depth = 3

result = g.iterative_deepening_dfs(start_node, goal_node, max_depth)
if result:
    print("Path found:", result)
else:
    print("No path found within depth limit")


# code from chatgpt
# Uninformed search strategy, IDS, combination between DFS_space and BFS_time for advantage
# with O(b^d) b is node and d is the depth that we found solution
# worst case O(b^m) where m is the maximum depth of the graph