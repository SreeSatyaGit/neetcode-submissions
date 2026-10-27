class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if mid * mid > x:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
                res = mid  # Store the closest valid floor square root
            else:
                return mid  # Exact square root found
                
        return res