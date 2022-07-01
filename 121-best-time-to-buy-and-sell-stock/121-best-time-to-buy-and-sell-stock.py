class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Maintain min price, update if current price is lower than min price
        # Maintain max profit, update if prices[i] - min price is greater than max profit
        
        maxProfit = 0
        minPrice = float('inf')
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if prices[i] - minPrice > maxProfit:
                maxProfit = max(maxProfit, prices[i] - minPrice)
        return maxProfit