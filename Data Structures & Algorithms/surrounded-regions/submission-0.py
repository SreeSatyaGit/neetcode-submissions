class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "E"  # Mark as safe (Edge-connected)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Run DFS for all 'O's on the border
        for r in range(ROWS):
            for c in range(COLS):
                if (
                    r in (0, ROWS - 1) or c in (0, COLS - 1)
                ) and board[r][c] == "O":
                    dfs(r, c)

        # 2. Update board: 'O' -> 'X', 'E' -> 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"