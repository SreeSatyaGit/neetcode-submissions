class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums, l, m, r):
            left, right = nums[l:m+1], nums[m+1:r+1]
            i, j, k = l, 0, 0
            
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    nums[i] = left[j]  # MISTAKE 1: Was nums[j] instead of left[j]
                    j += 1
                else:
                    nums[i] = right[k] # MISTAKE 1: Was nums[k] instead of right[k]
                    k += 1
                i += 1                 # MISTAKE 2: Missing i += 1
            
            while j < len(left):
                nums[i] = left[j]      # MISTAKE 1: Was nums[j] instead of left[j]
                j += 1
                i += 1                 # MISTAKE 2: Missing i += 1
                
            while k < len(right):
                nums[i] = right[k]     # MISTAKE 1: Was nums[k] instead of right[k]
                k += 1
                i += 1                 # MISTAKE 2: Missing i += 1

        def mergesort(nums, l, r):
            if l == r:
                return nums
            m = (l + r) // 2
            mergesort(nums, l, m)
            mergesort(nums, m + 1, r)
            merge(nums, l, m, r)
            return nums

        return mergesort(nums, 0, len(nums) - 1)