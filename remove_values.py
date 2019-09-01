class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        if len(nums) == 0:
            return 0
        
        insert = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[insert] = nums[i]
                insert += 1
        
        return insert
        