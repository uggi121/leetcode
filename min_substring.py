from collections import defaultdict

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l, r = 0, 0
        dict_t = defaultdict(int)
        for char in t:
            dict_t[char] += 1
            
        dict_s = defaultdict(int)
        #if len(s) > 0:
        #    dict_s[s[0]] += 1
        string = s
        
        atleast_one = False
        
        def check_s_r(dic1, dic2):
            return all(dic1[c] >= dic2[c] for c in dic2)
        
        #print(dict_t)
        while True:
            
            if check_s_r(dict_s, dict_t):
                atleast_one = True
                substring = s[l:r]
                if len(substring) < len(string):
                    string = substring
                dict_s[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r > len(s):
                    break
                dict_s[s[r - 1]] += 1
                
        if atleast_one:
            return string
        else:
            return ""
                
            