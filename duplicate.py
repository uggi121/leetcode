"""
Question:

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
"""

"""
Solution:

Initialize a set. Iterate through the array. If an element doesn't exist in the set, add it. 
If it already does, then it is a duplicate -> return True
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) < len(nums)