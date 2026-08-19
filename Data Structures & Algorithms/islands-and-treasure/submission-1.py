class Solution:

  def islandsAndTreasure(self, grid: List[List[int]]) -> None:
    if not grid or not grid[0]:
      return

    # All of the code below must be at this indentation level (4 spaces):
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()

    for r in range(ROWS):
      for c in range(COLS):
        if grid[r][c] == 0:
          q.append((r, c))

    INF = 2147483647
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
      r, c = q.popleft()

      for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
          grid[nr][nc] = grid[r][c] + 1
          q.append((nr, nc))