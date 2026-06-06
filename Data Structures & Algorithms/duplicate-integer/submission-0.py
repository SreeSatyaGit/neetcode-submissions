class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkNum = set()
        for i in nums:
            if i in checkNum:
                return True
            checkNum.add(i)
        return False

