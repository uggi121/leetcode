class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = len(matrix), len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    for k in range(cols):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'x'
        
        for j in range(cols):
            for i in range(rows):
                if matrix[i][j] == 0:
                    for k in range(rows):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'x'
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0
        