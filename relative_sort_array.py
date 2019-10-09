from collections import defaultdict

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dic = defaultdict(list)
        st = set(arr2);
        for i in arr1:
            if i in st:
                dic[i].append(i)
            else:
                dic[-1].append(i)
        
        result = []
        for i in arr2:
            result.extend(dic[i])
        
        result.extend(sorted(dic[-1]))
        return result
            
            