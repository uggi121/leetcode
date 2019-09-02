class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        
        visited = [[0 for j in range(cols)] for i in range(rows)]
        
        count = 0
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        stack = []
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    #print("DFS starting at ", i, j)
                    stack.append((i, j))
                    
                    while stack:
                        x, y = stack.pop()
                        #print("Visiting", x, y)
                        visited[x][y] = 1
                        for dr in dirs:
                            _x, _y = x + dr[0], y + dr[1]
                            if (0 <= _x and _x < rows and 0 <= _y and _y < cols
                               and not visited[_x][_y] and grid[_x][_y] == '1'):
                                stack.append((_x, _y))
                        
        
        return count