class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)

            for prev in preMap[crs]:
                if not dfs(prev):
                    return False
            
            visiting.remove(crs)

            preMap[crs] = []
            return True
        

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True