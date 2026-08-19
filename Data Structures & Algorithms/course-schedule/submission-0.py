class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Track courses currently in the active DFS call stack
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False  # Cycle detected
            if preMap[crs] == []:
                return True   # Course has no prerequisites / already verified

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            preMap[crs] = []  # Optimization: mark course as fully processed
            return True

        # Check every course (handles disconnected components)
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True