class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        res = right

        while left <= right:
            mid = (left + right) //2

            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid -1) //mid
            
            if total_hours <= h:
                res = mid
                right = mid -1 

            else:
                left = mid + 1
        return res