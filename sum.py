"""
Similar to staircase/steps problem - Store solution to each subproblem and add the parts to get the whole.
"""

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        memo = {}
        memo[0] = 1
        
        def tgt(n):
            #print(n)
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            else:
                steps = [tgt(n - x) for x in nums]
                memo[n] = sum(steps)
                return memo[n]
        
        return tgt(target)
            