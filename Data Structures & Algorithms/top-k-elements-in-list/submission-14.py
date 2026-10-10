class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) +1
        
        freqBuckets = [[] for _ in range(len(nums) + 1)]
        for num,freq in counter.items():
            freqBuckets[freq].append(num)
        
        res = []
        for i in range(len(freqBuckets)-1,0,-1):
            for num in freqBuckets[i]:
                res.append(num)
            if len(res) == k:
                return res