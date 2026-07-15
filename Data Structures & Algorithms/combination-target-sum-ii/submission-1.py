from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates to group duplicates together
        candidates.sort()
        res = []
        
        def dfs(i: int, curr: List[int], target: int):
            # Base Case 1: Success
            if target == 0:
                res.append(list(curr))
                return
            
            # Base Case 2: Failure boundaries
            if target < 0 or i >= len(candidates):
                return
            
            # Decision 1: Include candidates[i]
            curr.append(candidates[i])
            # Move to i + 1 because we cannot reuse the same exact element
            dfs(i + 1, curr, target - candidates[i])
            curr.pop() # Backtrack
            
            # Decision 2: Skip candidates[i] AND all its duplicates
            # Move index past any element equal to candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
                
            # Recurse on the next unique element
            dfs(i + 1, curr, target)
            
        dfs(0, [], target)
        return res