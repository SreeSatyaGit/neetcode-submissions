from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        
        # 1. Initialize queue with all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
                    
        # If there are no fresh oranges to begin with, 0 minutes have elapsed
        if fresh == 0:
            return 0
            
        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 2. Perform BFS level-by-level (each level represents 1 minute)
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If neighbor is a fresh fruit, rot it and add to queue
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
                        
            time += 1
            
        # 3. Return time if all fresh oranges rotted, otherwise -1
        return time if fresh == 0 else -1