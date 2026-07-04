class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            countMap[num] = 1 + countMap.get(num,0)
        
        bucket = [[] for _ in range(len(nums)+1)]

        for num,frequency in countMap.items():
            bucket[frequency].append(num)
        
        result = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        