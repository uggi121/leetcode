class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r = 0, 0
        chars = set()
        max_length = 0
        length = len(s)
        
        while r < length:
            if s[r] in chars:
                chars.remove(s[l])
                l += 1
                
            else:
                chars.add(s[r])
                r += 1
                if r - l > max_length:
                    max_length = r - l
        
        return max_length
            