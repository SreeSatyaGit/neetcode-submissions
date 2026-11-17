class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum = max_sum =  nums[0]
        for n in nums[1:]:
            currentsum = max(n,currentsum+n)
            max_sum = max(max_sum,currentsum)
        return max_sum
            