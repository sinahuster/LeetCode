"""
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

Constraints:
1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000
"""

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        @cache
        def dp(row, col):
            if row == len(nums2) or col == len(nums1):
                return 0
            
            row_skip = dp(row + 1, col)
            col_skip = dp(row, col + 1)
            used =  nums1[col] * nums2[row] + dp(row + 1, col + 1)

            return max(row_skip, col_skip, used)

        return dp(0,0)
    
# The time and space complexity O(n * m), where n and m are the length of nums1 and nums2 respectively. 