"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        result = []

        for i in nums1:
            if i not in seen:
                seen[i] =  i
        
        for j in nums2:
            if j in seen and j not in result:
                result.append(j)

        return result