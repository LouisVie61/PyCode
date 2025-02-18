class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)  # Concise way to add edges

    def depth_limited_search(self, node, goal, depth_limit):
        """Recursive DLS without a persistent visited set to allow proper backtracking."""
        if node == goal:
            return [node]
        if depth_limit <= 0:
            return None
        if node not in self.graph:  # If no outgoing edges, return
            return None

        for neighbor in self.graph[node]:
            path = self.depth_limited_search(neighbor, goal, depth_limit - 1)
            if path:
                return [node] + path  # Append current node to path
        return None

    def iterative_deepening_dfs(self, start, goal, max_depth):  # Allow infinite search
        visited = set()  # Prevent cycles across iterations (not in DLS)

        for depth in range(1, max_depth + 1):  # Increase depth limit gradually
            visited.clear()  # Reset visited set for each new depth limit
            path = self.depth_limited_search(start, goal, depth)
            if path:
                return path
        return None


# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 7)
g.add_edge(7, 0)  # Cycle

start_node = 0
goal_node = 6
max_depth = 4  # Increased to ensure solution is found

result = g.iterative_deepening_dfs(start_node, goal_node, max_depth)
print("Path found:", result if result else "No path found within depth limit")

#
