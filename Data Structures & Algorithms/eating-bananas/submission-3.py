class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1, max(piles)
        res = right

        while left <= right:
            mid = (left + right)//2

            total_hours = 0

            for p in piles:
                total_hours += (p + mid - 1)//mid

            if total_hours <= h:
                res = mid
                right = mid -1
            else:
                left = mid +1
        return res