"""
Question:

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

"""
Solution: 

Initialize an empty hash-table/dict to store (value, index) pairs and iterate through the elements of the given array. 
For each element, check if (target - element) exists in the hash-table. 
If it does, then the index of the current element and the value of the key-value pair of the dict form the necessary indices.

The solution runs in O(n) time and requires O(n) extra space. 
If the input array is sorted, the problem breaks down into a case requiring O(1) extra space.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]
            else:
                dic[num] = i
                
        