"""
Bad solution - lots of repeated code. Can make it much shorter by running for loop m * n times where m, n = rows, cols of matrix.
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
        
        result = []
        
        def dfs(i, j, di):
            visited[i][j] = 1
            result.append(matrix[i][j])
            if di == 0:
                if j + 1 < cols:
                    if not visited[i][j + 1]:
                        dfs(i, j + 1, 0)
                    elif not visited[i + 1][j]:
                        dfs(i + 1, j, 1)
                else:
                    if i + 1 < rows and not visited[i + 1][j]:
                        dfs(i + 1, j, 1)
            elif di == 1:
                if i + 1 < rows:
                    if not visited[i + 1][j]:
                        dfs(i + 1, j, 1)
                    elif not visited[i][j - 1]:
                        dfs(i, j - 1, 2)
                else:
                    if j - 1 >= 0 and not visited[i][j - 1]:
                        dfs(i, j - 1, 2)
            elif di == 2:
                if j - 1 >= 0:
                    if not visited[i][j - 1]:
                        dfs(i, j - 1, 2)
                    elif not visited[i - 1][j]:
                        dfs(i - 1, j, 3)
                else:
                    if i - 1 >= 0 and not visited[i - 1][j]:
                        dfs(i - 1, j, 3)
            elif di == 3:
                if i - 1 >= 0:
                    if not visited[i - 1][j]:
                        dfs(i - 1, j, 3)
                    elif not visited[i][j + 1]:
                        dfs(i, j + 1, 0)
                else:
                    if j + 1 < cols and not visited[i][j + 1]:
                        dfs(i, j + 1, 0)        
        
        dfs(0, 0, 0)
        
        return result