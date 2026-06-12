"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_start = 0
        col_start = 0
        row_end = len(matrix) - 1
        col_end = len(matrix[0]) - 1

        while row_start < row_end:
            row_mid = (row_start + row_end) // 2
            if matrix[row_mid][col_end] == target:
                return True
            if matrix[row_mid][col_end] < target:
                row_start = row_mid + 1
            else:
                row_end = row_mid

        while col_start <= col_end:
            col_mid = (col_start + col_end) // 2
            if matrix[row_start][col_mid] == target:
                return True
            if matrix[row_start][col_mid] < target:
                col_start = col_mid + 1
            else:
                col_end = col_mid - 1

        return False
    
# This has time comeplexity O(log m * n), where n is the number of cols and m is the number of rows,
# and space complexity of O(1)