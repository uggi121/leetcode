import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if not nums:
            return 0
        
        h = []
        
        for i in range(len(nums)):
            if len(h) < k:
                heapq.heappush(h, nums[i])
            else:
                if nums[i] > h[0]:
                    heapq.heappushpop(h, nums[i])
        
        return h[0]
        