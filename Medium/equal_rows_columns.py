"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Constraints:
n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 10^5
"""

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        seen = {}
        count = 0

        for i in range(len(grid)):
            if tuple(grid[i]) in seen:
                seen[tuple(grid[i])] += 1
            else:
                seen[tuple(grid[i])] = 1

        
        for i in range(len(grid[0])):
            column = []
            for j in range(len(grid)):
                column.append(grid[j][i])
            count += seen.get(tuple(column), 0)

        return count

"""
This has time and space complexity O(n^2) as it is a square grid. 
There are n rows and it takes O(n) time to convert a row to a tuple, so we have O(n^2) time. 
seen has up to n keys and each key is a tuple of n elements. 
"""