"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        cols = len(grid[0])
        rows = len(grid)
        seen = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(x, y):
            if (x < 0 or y < 0 or x >= rows or y >= cols 
                or grid[x][y] == 0 or (x,y) in seen):
                return 0

            seen.add((x, y))
            area = 1
            for dx, dy in directions:
                area += dfs(x + dx, y + dy)
            return area

        ans = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == 1:
                    ans = max(ans, dfs(row, col))

        return ans


# This has time and space complexity O(n)