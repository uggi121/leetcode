"""
Longest increasing subsequence- Dynamic Programming.

Todo : Clean and format code.
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        lis = {}
        for i in range(len(nums)):
            found = False
            max_value = 1
            for j in range(i):
                
                if nums[j] < nums[i]:
                    found = True
                    if j in lis and lis[j] >= max_value:
                        max_value = lis[j]
            lis[i] = max_value + 1
            if not found:
                lis[i] = 1
        
        if len(lis) == 0:
            return 0
        return max(lis.values())
            
