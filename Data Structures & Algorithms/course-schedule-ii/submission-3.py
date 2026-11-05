class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashMap = {c:[] for c in range(numCourses)}
        output = []
        for crs,pre in prerequisites:
            hashMap[crs].append(pre)

        visit , cycle = set(),set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in hashMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for crs in range(numCourses):
            if dfs(crs) == False: return []
        return output