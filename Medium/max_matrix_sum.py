"""
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. 
Return the maximum sum of the matrix's elements using the operation mentioned above.

Constraints:
n == matrix.length == matrix[i].length
2 <= n <= 250
-10^5 <= matrix[i][j] <= 10^5
"""


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        total = 0
        negative = 0
        smallest = float('inf')

        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    negative += 1
                if abs(matrix[i][j]) < smallest:
                    smallest = abs(matrix[i][j])
                total += abs(matrix[i][j])

        if negative % 2 != 0:
            total -= 2 * smallest 

        return total 

        # Find the number of negative numbers 
        # If there is an even number, there will be a way to swap all to positive
        # If odd number, find the number with the smallest absolute value, use as negative
        # Add together all the numbers 


# This has time complexity O(n^2)
# and constant space complexity O(1)