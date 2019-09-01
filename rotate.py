class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        mat = matrix
        for i in range(n // 2):
            for j in range(i, (n - 1 - i)):
                mat[i][j], mat[j][n - i - 1], mat[n - i - 1][n - j - 1], mat[n - j - 1][i] = mat[n - j - 1][i], mat[i][j], mat[j][n - i - 1], mat[n - i - 1][n - j - 1]
        
        
                
                
        