class Solution:

  def subsetXORSum(self, nums: list[int]) -> int:

    def dfs(i: int, total: int) -> int:
      if i == len(nums):
        return total
      include = dfs(i + 1, total ^ nums[i])
      exclude = dfs(i + 1, total)
      return include + exclude

    return dfs(0, 0)