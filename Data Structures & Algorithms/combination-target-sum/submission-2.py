from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i: int, cur: List[int], target: int):
            if target == 0:
                res.append(list(cur))
                return
            

            if target < 0 or i >= len(nums):
                return
            
            cur.append(nums[i])
            dfs(i,cur,target - nums[i])
            cur.pop()

            dfs(i+1,cur, target)


        dfs(0,[],target)
        return res