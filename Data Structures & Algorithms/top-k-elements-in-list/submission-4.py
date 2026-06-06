import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [0]*2001

        for num in nums:
            arr[num] += 1
        
        topk_indices_in_arr = np.argpartition(np.array(arr), -k)[-k:].tolist()
        topk_indices_in_arr = [i-2001 if i >1000 else i for i in topk_indices_in_arr]
        return topk_indices_in_arr
            