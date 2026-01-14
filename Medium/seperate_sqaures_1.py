"""
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted multiple times.

Constraints:
1 <= squares.length <= 5 * 104
squares[i] = [xi, yi, li]
squares[i].length == 3
0 <= xi, yi <= 109
1 <= li <= 109
The total area of all the squares will not exceed 1012.
"""

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        squares.sort(key=lambda x: x[1])
        low = min(square[1] for square in squares) # lowest possible y value 
        high = max(square[1] + square[2] for square in squares) # highest
        total_area = sum([square[2] ** 2 for square in squares])

        while high - low > 1e-5:
            mid = low + (high - low) / 2
            area_below = 0.0

            for square in squares:
                bottom = square[1]
                side = square[2]
                top = bottom + side

                if top <= mid:
                    area_below += side ** 2
                elif bottom >= mid:
                    break
                else:
                    height_below = mid - bottom
                    area_below += height_below * side

            if area_below >= total_area / 2:
                high = mid
            else:
                low = mid 

        return low
    
    # This has time O(n log n) and space complexity O(1)