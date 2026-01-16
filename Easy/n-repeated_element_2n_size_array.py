"""
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique values, n of which occur exactly once in the array.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

Constraints:
2 <= n <= 5000
nums.length == 2 * n
0 <= nums[i] <= 10^4
nums contains n + 1 unique elements and one of them is repeated exactly n times.
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = {}

        length = len(nums)

        for i in range(length):
            if nums[i] in seen:
                return nums[i]
            seen[nums[i]] = 1
        return -1
    
# This has time complexity O(2n), where 2n is the length of nums, and space complexity O(1)