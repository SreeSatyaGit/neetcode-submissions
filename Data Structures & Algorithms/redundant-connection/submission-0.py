from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(source, target, visited):
            if source == target:
                return True
            visited.add(source)
            for neighbor in adj[source]:
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            return False

        for u, v in edges:
            visited = set()
            # If path already exists between u and v, this edge creates a cycle
            if u in adj and v in adj and dfs(u, v, visited):
                return [u, v]
            
            # Otherwise, add edge to graph
            adj[u].append(v)
            adj[v].append(u)