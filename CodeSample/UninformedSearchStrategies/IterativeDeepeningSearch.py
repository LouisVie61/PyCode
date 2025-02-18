class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)  # More concise way to add edges

    def depth_limited_search(self, node, goal, depth_limit, visited=None):  # Add visited set
        if visited is None:
            visited = set()
        if node in visited: # Check if node is already visited
            return None
        visited.add(node) # Add node to visited set

        if node == goal:
            return [node]
        if depth_limit <= 0:
            return None

        if node not in self.graph:
            return None

        for neighbor in self.graph[node]:
            path = self.depth_limited_search(neighbor, goal, depth_limit - 1, visited)
            if path:
                return [node] + path
        return None

    def iterative_deepening_dfs(self, start, goal, max_depth): # Allow infinite search
        for depth in range(1, max_depth + 1): # If max_depth is infinity, this will loop indefinitely
            path = self.depth_limited_search(start, goal, depth)
            if path:
                return path
        return None

# Example usage (same as before)
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(3, 7)
g.add_edge(7, 0) # Add a cycle to demonstrate the visited set

start_node = 0
goal_node = 6
max_depth = 4 # Increased to find the solution with the new cycle

result = g.iterative_deepening_dfs(start_node, goal_node, max_depth)
if result:
    print("Path found:", result)
else:
    print("No path found within depth limit")

goal_node = 7
result = g.iterative_deepening_dfs(start_node, goal_node) # No depth limit
if result:
    print("Path found:", result)
else:
    print("No path found within depth limit")


# code from chatgpt
# Uninformed search strategy, IDS, combination between DFS_space and BFS_time for advantage
# with O(b^d) b is node and d is the depth that we found solution
# worst case O(b^m) where m is the maximum depth of the graph