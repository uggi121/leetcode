"""
There is one way to reach the first step (One 1-weighted step).
There are two ways to reach the second step (Two 1-weighted steps or one 2-weighted step).

For step number n, we can reach it from step number n - 1 or step n - 2. This is a straightforward recursive solution.
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        memo[1] = 1
        memo[2] = 2
        def helper(m):
            if m not in memo:
                memo[m] = helper(m - 1) + helper(m - 2)
            return memo[m]
        return helper(n)