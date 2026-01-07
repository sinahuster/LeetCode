"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). 
You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. 
You cannot step into a cell with a wall, and you cannot step outside the maze. 
Your goal is to find the nearest exit from the entrance. 
An exit is defined as an empty cell that is at the border of the maze. 
The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists

Constraints:
maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.
"""

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        def valid(row, col):
            return 0 <= row < n and 0 <= col < m and maze[row][col] == "."

        def exit(row, col):
            return ((row == 0 or row == n - 1 or col == 0 or col == m - 1) 
                    and [row, col] != entrance)
        
        directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
        n = len(maze)
        m = len(maze[0])
        seen = set()
        queue = deque([(entrance[0], entrance[1], 0)])

        while queue:
            row, col, steps = queue.popleft()
            if exit(row, col):
                return steps

            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))

        return -1 

# This has time and space complexity O(n * m) which are the rows and columns of the maze
