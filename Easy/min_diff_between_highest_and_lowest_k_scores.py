"""
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. 
You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.

Constraints:
1 <= k <= nums.length <= 1000
0 <= nums[i] <= 10^5
"""


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        if k == 1:
            return 0

        i = 0
        j = k - 1
        min_diff = float("inf")

        while j < len(nums):
            diff = nums[j] - nums[i]
            min_diff = min(min_diff, diff)
            j += 1 
            i += 1
            
        return min_diff


# This has time complexity O(n) and space comeplxity O(1)