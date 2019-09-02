from collections import defaultdict
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if not nums:
            return []
        
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        
        h = []
        
        for i in counts:
            h.append((-counts[i], i))
        
        heapq.heapify(h)
        
        result = []
        
        for i in range(k):
            result.append(heapq.heappop(h)[1])
        
        return result
            