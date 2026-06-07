class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        seen = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val != '.':
                    row_marker = f"{val} in row {r}"
                    col_marker = f"{val} in col {c}"
                    block_marker = f"{val} in block {r//3} - {c//3}"

                    if row_marker in seen or col_marker in seen or block_marker in seen:
                        return False
                    
                    seen.update((row_marker,col_marker,block_marker))
                
        return True