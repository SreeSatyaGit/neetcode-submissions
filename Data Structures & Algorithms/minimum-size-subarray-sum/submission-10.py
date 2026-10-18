class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        left = 0
        res = len(nums) +1
        currentsum = 0
        for right in range(len(nums)):
            currentsum += nums[right]

            while currentsum >= target:
                res = min(right - left +1 ,res)
                currentsum -= nums[left]
                left +=1
        return res