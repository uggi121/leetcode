"""
Spiral print - better solution
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        result = []
        i, j = 0, 0
        current_dir = 0
        for k in range(rows * cols):
            visited[i][j] = 1
            result.append(matrix[i][j])
            for _ in range(4):
                direction = dirs[current_dir]
                shift_i, shift_j = direction[0], direction[1]
                next_i, next_j = i + shift_i, j + shift_j
                if ((0 <= next_i and next_i < rows 
                            and 0 <= next_j and next_j < cols)
                            and not visited[next_i][next_j]):
                    i, j = next_i, next_j
                    break
                else:
                    current_dir = (current_dir + 1) % 4
                    
        return result
        
        