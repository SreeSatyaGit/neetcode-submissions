class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list: prerequisite b -> course a
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
            
        output = []
        visit, cycle = set(), set()
        
        def dfs(crs):
            if crs in cycle:
                return False  # Cycle detected
            if crs in visit:
                return True   # Already fully processed
            
            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            
            visit.add(crs)
            output.append(crs)
            return True
            
        for c in range(numCourses):
            if not dfs(c):
                return []
                
        return output