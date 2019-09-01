class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 1:
            return len(nums)
        
        value = None
        insert = 0
        
        for i in range(len(nums)):
            if nums[i] != value:
                value = nums[i]
                nums[insert] = value
                insert += 1
            
        
        return insert
            
        