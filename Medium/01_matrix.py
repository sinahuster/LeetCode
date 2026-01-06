"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        def valid(row, col):    
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1

        m = len(mat)
        n = len(mat[0])
        queue = deque()
        seen = set()

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))
                    seen.add((row, col))

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while queue:
            row, col, steps = queue.popleft()
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    queue.append((next_row, next_col, steps + 1))
                    seen.add((next_row, next_col))
                    mat[next_row][next_col] = steps

        return mat
    

# This has time and space complexity O(n * m)