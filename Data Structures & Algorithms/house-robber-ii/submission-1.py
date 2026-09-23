class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def houserob(numbers):
            rob1,rob2 = 0,0
            for n in numbers:
                temp = max(n+rob1,rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(houserob(nums[1:]), houserob(nums[:-1]))
        