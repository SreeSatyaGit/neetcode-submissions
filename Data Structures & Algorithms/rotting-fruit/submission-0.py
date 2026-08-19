from collections import deque
from typing import List


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        time = 0

        # Step 1: Initialize queue with all rotten fruits and count fresh fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # Step 2: Multi-source BFS
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1