class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            l = i +1

            if i > 0 and nums[i] == nums[i-1]:
                continue
            r = len(nums) - 1
            while l < r:
                currsum = nums[i] + nums[l] + nums[r]
                if currsum < 0:
                    l +=1
                elif currsum > 0:
                    r -=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l +=1
                    r -=1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -=1
        return res





