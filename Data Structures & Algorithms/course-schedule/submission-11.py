class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {c:[] for c in range(numCourses)}

        for crs,prev in prerequisites:
            prevMap[crs].append(prev)
        
        cycle,visit = set(),set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for prev in prevMap[crs]:
                if dfs(prev) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
