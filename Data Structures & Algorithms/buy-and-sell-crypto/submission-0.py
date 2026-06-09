class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        min_price = float('inf')
        max_price= 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_price:
                max_price = price - min_price
        return max_price