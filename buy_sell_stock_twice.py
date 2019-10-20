class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        left_profit = [0] * len(prices)
        
        min_so_far, max_profit, max_profit_total = float('inf'), 0, 0
        
        for i, price in enumerate(prices):
            min_so_far = min(price, min_so_far)
            max_profit = max(max_profit, price - min_so_far)
            left_profit[i] = max_profit
            
        max_so_far = float('-inf')    
        for i, price in reversed(list(enumerate(prices))):
            max_so_far = max(max_so_far, price)
            profit = max_so_far - price
            prev_profit = left_profit[i - 1] if i > 0 else 0
            max_profit_total = max(max_profit_total,
                                   prev_profit + profit)
        
        return max_profit_total