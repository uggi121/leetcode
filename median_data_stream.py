import heapq

class MedianFinder(object):
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap, self.min_heap = [], []
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.max_heap, -num)
        number = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, number)
        
        if len(self.min_heap) > len(self.max_heap):
            number = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -number)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            if self.min_heap and self.max_heap:
                return float(-self.max_heap[0] + self.min_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()