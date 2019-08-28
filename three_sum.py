"""
Sort the input array. Run an outer loop through all elements. Run an inner loop with two indices, left and right.

Initialize left to one value above the outer index, and initialize right to the right most end of the array.
Check step-by-step for the target sum. If the sum is reached, add it to the solutions set. Otherwise, adjust indices accordingly.
"""

from collections import defaultdict

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        solutions = set()
        for idx, num in enumerate(nums):
            l, r = idx + 1, len(nums) - 1
            target = -num
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif idx != l and idx != r:
                    solutions.add(tuple([nums[l], nums[r], num]))
                    l += 1
                    r -= 1
                else:
                    l += 1
        
        return solutions
        