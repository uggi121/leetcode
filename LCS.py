"""
Longest common subsequence: Dynamic programming
"""

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        lcs = [] 
        for i in range(len(text1)):
            lcs.append([0] * len(text2))
        def get_lcs(i, j):
            if i < 0 or j < 0:
                return 0
            if lcs[i][j] != 0 and i != 0 and j != 0:
                return lcs[i][j]
            elif text1[i] == text2[j]:
                lcs[i][j] = get_lcs(i - 1, j - 1) + 1
            else:
                lcs[i][j] = max(get_lcs(i, j - 1), get_lcs(i - 1, j))
            return lcs[i][j]
        
        return get_lcs(len(text1) - 1, len(text2) - 1)
        
        