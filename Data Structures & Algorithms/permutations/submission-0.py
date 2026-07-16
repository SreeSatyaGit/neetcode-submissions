class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        numset = set()
        subset = []
        def dfs():
            if len(subset) == len(nums):
                res.append(subset[:])
                return

            for i,num in enumerate(nums):
                if num not in numset:
                    subset.append(num)
                    numset.add(num)
                    dfs()
                    numset.remove(num)
                    subset.pop()


        
        dfs()
        return res

