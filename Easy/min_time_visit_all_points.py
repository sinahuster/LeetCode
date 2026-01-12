"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
 
Constraints:
points.length == n
1 <= n <= 100
points[i].length == 2
-1000 <= points[i][0], points[i][1] <= 1000
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        current = points[0]
        length = len(points)
        steps = 0

        for i in range(1, length):
            x_diff = abs(points[i][0] - current[0])
            y_diff = abs(points[i][1] - current[1])
            steps += max(x_diff, y_diff)
            current = points[i]
    
        return steps
    
# This has time complexity O(n) and space complexitu O(1)