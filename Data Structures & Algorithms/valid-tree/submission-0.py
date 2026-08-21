class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build undirected adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False  # Cycle detected
            
            visit.add(node)
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue  # Skip the edge going back to parent
                if not dfs(neighbor, node):
                    return False
            return True

        # Start traversal from node 0 and ensure no cycles
        if not dfs(0, -1):
            return False

        # Ensure all nodes are connected
        return len(visit) == n