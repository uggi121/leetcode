class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        left_prods = []
        right_prods = []
        
        
        for idx, num in enumerate(nums):
            if idx != 0:
                left_prods.append(num * left_prods[idx - 1])
            else:
                left_prods.append(num)
        
        right_idx = len(nums) - 1
        
        while right_idx >= 0:
            if right_idx != len(nums) - 1:
                right_prods.append(nums[right_idx] 
                                * right_prods[len(nums) - 2 - right_idx])
            else:
                right_prods.append(nums[right_idx])
            right_idx -= 1
        
        right_prods.reverse()
        
        result = []
        
        for i in range(len(nums)):
            if i == 0:
                result.append(right_prods[1])
            elif i == len(nums) - 1:
                result.append(left_prods[-2])
            else:
                result.append(left_prods[i - 1] * right_prods[i + 1])
        
        return result
        