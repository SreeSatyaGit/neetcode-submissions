class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        buckets = [[] for _ in range(500001)]

        for num in nums:
            if num >= 0:
                buckets[50000 + num].append(num) 
            else:
                buckets[50000 + num].append(num)

        out = []

        for bucket in buckets:
            for i in range(len(bucket)):
                out.append(bucket[i])    

        return out