"""
Question:

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""

"""
Solution:

If the array is of length 1, then the profit is 0.

Suppose the length of the array is > 1 and a, b are two successive indices.
If prices[b] < prices[a], then for all prices succeeding b, buying on day b gives greater profits than buying on day a.

Initialize two pointers, both at index 0.

If b > a and price[b] < price[a], then reset the pointers to index a.
Else, keep pushing one pointer to the right and update the max value.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 0
        max_so_far = 0
        
        while True:
            r += 1
            if r >= len(prices):
                break
            if prices[r] < prices[l]:
                l = r
                continue
            diff = prices[r] - prices[l]
            if diff > max_so_far:
                max_so_far = diff
        
        return max_so_far
                
        