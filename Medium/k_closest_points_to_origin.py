"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Constraints:
1 <= k <= points.length <= 10^4
-10^4 <= xi, yi <= 10^4
"""

import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(heap, (-distance, point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [coords[1] for coords in heap]
    

# This has time complexity O(n log k), where n is the length of points, 
# and space complexity O(k)