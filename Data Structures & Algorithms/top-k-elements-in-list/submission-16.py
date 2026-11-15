class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        countnums = Counter(nums)

        freq = [[]for _ in range(len(nums)+1)]

        for val,cnt in countnums.items():
            freq[cnt].append(val)
        
        for f in range(len(freq)-1,-1,-1):
            for n in freq[f]:
                res.append(n)
                if len(res) == k:
                    return res

