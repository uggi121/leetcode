class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = [-1] * (len(nums))
        if len(nums) > 0:
            memo[0] = nums[0]
        
        def f(n):
            if n < 0:
                return 0
            if memo[n] >= 0:
                return memo[n]
            else:
                memo[n] = max(f(n - 1), f(n - 2) + nums[n])
                return memo[n]
        #print(memo)
        f(len(nums) - 1)
        if len(memo) > 0:
            return max(memo)
        return 0
            
        