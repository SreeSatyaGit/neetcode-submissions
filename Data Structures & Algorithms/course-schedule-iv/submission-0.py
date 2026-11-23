from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prerequisites:
            adj[pre].append(crs)

        reachable = [[False] * numCourses for _ in range(numCourses)]

        for start in range(numCourses):
            visited = set()

            def dfs(curr: int) -> None:
                for nxt in adj[curr]:
                    if nxt not in visited:
                        visited.add(nxt)
                        reachable[start][nxt] = True
                        dfs(nxt)

            dfs(start)

        return [reachable[u][v] for u, v in queries]