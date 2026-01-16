"""
There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical fences given in arrays hFences and vFences respectively.

Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1, vFences[i]) to (m, vFences[i]).

Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible to make a square field.

Since the answer may be large, return it modulo 109 + 7.

Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). 
These fences cannot be removed.

Constraints:
3 <= m, n <= 10^9
1 <= hFences.length, vFences.length <= 600
1 < hFences[i] < m
1 < vFences[i] < n
hFences and vFences are unique.
"""

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.sort()
        vFences.sort()
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]

        h_diff = {}
        v_diff = {}

        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_diff[hFences[j] - hFences[i]] = 1
        
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_diff[vFences[j] - vFences[i]] = 1       

        max_common = -1

        for value in h_diff:
            if value in v_diff:
                if value > max_common:
                    max_common = value
        
        if max_common == -1:
            return -1 

        return (max_common * max_common) % (10 ** 9 + 7)
    
# This has time and space complexity O(m^2 + n^2)