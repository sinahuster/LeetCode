"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

        def dfs(row, col):
            for x, y in directions:
                next_row, next_col = row + x, col + y
                if valid(next_row, next_col) and (next_row, next_col) not in land:
                    land.add((next_row, next_col))
                    dfs(next_row, next_col)
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n = len(grid[0])
        m = len(grid)
        land = set()
        ans = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in land:
                    ans += 1
                    land.add((row, col))
                    dfs(row, col)

        return ans
    
# This has time and space complexity O(n + m)