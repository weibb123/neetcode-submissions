class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        next2buy, next1buy = 0, 0
        next2sell, next1sell = 0, 0

        for i in range(n - 1, -1, -1):
            current_buy = max(next1sell - prices[i], next1buy)
            current_sell = max(next2buy + prices[i], next1sell)
            next2buy, next1buy = next1buy, current_buy
            next2sell, next1sell = next1sell, current_sell
        
        return current_buy
        
        