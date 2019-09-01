from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        def get_counts(word):
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord('a')] += 1
            return tuple(counts)
        
        counts = defaultdict(list)
        for word in strs:
            cts = get_counts(word)
            counts[cts].append(word)
            
        return list(counts.values())