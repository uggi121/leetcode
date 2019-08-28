"""
Coin Change Solution-1:

Memoize and go through all cases in the tree.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = {}
        memo[0] = 0
        
        def helper(amt):
            #print(amt)
            if amt < 0:
                return -1
            if amt in memo:
                return memo[amt]
            else:
                new_amounts = [amt - x for x in coins]
                values = list(filter(lambda x: x >= 0, [helper(x) for x in new_amounts]))
                if len(values) == 0:
                    memo[amt] = -1
                else:
                    memo[amt] = min(values) + 1
                return memo[amt]
            
        return helper(amount)      
                
                
                
                
                
            