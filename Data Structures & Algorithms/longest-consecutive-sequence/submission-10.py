class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        length = 0
        longest = 0
        for n in nums:
            if (n-1) not in numset:
                length = 1

                while n + length in numset:
                    length +=1
            longest = max(longest,length)
        return longest