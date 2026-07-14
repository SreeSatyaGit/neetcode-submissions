from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i: int, cur: List[int], target: int):
            # Base Case 1: If target is met, we found a valid combination
            if target == 0:
                res.append(list(cur))
                return
            
            # Base Case 2: Out of bounds or exceeded target sum
            if target < 0 or i >= len(nums):
                return
            
            # Decision 1: Include nums[i] (and allow it to be chosen again)
            cur.append(nums[i])
            dfs(i, cur, target - nums[i])
            cur.pop() # Backtrack to explore other choices
            
            # Decision 2: Do not include nums[i] (move to the next number)
            dfs(i + 1, cur, target)
            
        dfs(0, [], target)
        return res