class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [[1 if i == j else 0 for j in range(length)] for i in range(length)]
            
        def memo(i, j):
            if i > j:
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            else:
                if s[i] == s[j]:
                    dp[i][j] = memo(i + 1, j - 1) + 2
                else:
                    dp[i][j] = max(memo(i + 1, j), memo(i, j - 1))
                return dp[i][j]
        
        return memo(0, length - 1)
        