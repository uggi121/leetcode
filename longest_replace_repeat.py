from collections import defaultdict

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        l, r = 0, 0
        max_length = 0
        counts = defaultdict(int)
        
        def get_max_key(dic):
            ky = 0
            dic[0] = 0
            for key in dic:
                if dic[key] > dic[ky]:
                    ky = key
            return ky
        
        add = True
        while r < len(s) and l < len(s):
            
            if add:
                counts[s[r]] += 1
            length_substring = r - l + 1
            maxx = get_max_key(counts)
            if counts[maxx] >= length_substring - k:
                r += 1
                add = True
                if r - l > max_length:
                    max_length = r - l
            else:
                add = False
                counts[s[l]] -= 1
                l += 1
            
        
        return max_length
            