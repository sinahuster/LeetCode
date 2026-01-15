"""
You are given the two integers, n and m and two integer arrays, hBars and vBars. 
The grid has n + 2 horizontal and m + 2 vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from 1.

You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. 
Note that other bars are fixed and cannot be removed.

Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).

Constraints:
1 <= n <= 10^9
1 <= m <= 10^9
1 <= hBars.length <= 100
2 <= hBars[i] <= n + 1
1 <= vBars.length <= 100
2 <= vBars[i] <= m + 1
All values in hBars are distinct.
All values in vBars are distinct.
"""

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()

        h_longest = v_longest = 1
        h_length = v_length = 1

        for i in range(len(hBars) - 1):
            if hBars[i] == hBars[i + 1] - 1:
                h_length += 1
                if h_length > h_longest:
                    h_longest = h_length
            else:
                h_length = 1
            
        for i in range(len(vBars) - 1):
            if vBars[i] == vBars[i + 1] - 1:
                v_length += 1
                if v_length > v_longest:
                    v_longest = v_length
            else:
                v_length = 1
            
        max_side = min(h_longest, v_longest) + 1

        return max_side * max_side 
