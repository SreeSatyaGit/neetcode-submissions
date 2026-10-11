class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        res = 0
        for i in range(len(prices)):
            right = i
            while right < len(prices) :
                diff = prices[right] - prices[i] 
                if diff > 0:
                    profit = max(profit,diff)
                right += 1
        return profit       
                
                


