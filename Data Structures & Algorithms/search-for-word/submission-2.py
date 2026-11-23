from typing import List


class Solution:

  def exist(self, board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])

    def dfs(r: int, c: int, idx: int) -> bool:
      if idx == len(word):
        return True
      if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[idx]:
        return False

      temp = board[r][c]
      board[r][c] = "#"  # Mark visited in current path

      found = (
          dfs(r + 1, c, idx + 1)
          or dfs(r - 1, c, idx + 1)
          or dfs(r, c + 1, idx + 1)
          or dfs(r, c - 1, idx + 1)
      )

      board[r][c] = temp  # Backtrack
      return found

    for r in range(rows):
      for c in range(cols):
        if board[r][c] == word[0] and dfs(r, c, 0):
          return True

    return False