"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 10^6
1 <= k <= min(50, nums.length)
"""

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        if k == 1:
            return sum(nums)
        if k == len(nums):
            return max(nums)
        
        def check(minimized):
            partitions = 1
            total = 0
            for i in range(len(nums)):
                if nums[i] > minimized:
                    return k + 1
                if total + nums[i] > minimized:
                    partitions += 1
                    total = 0
                total += nums[i]
            return partitions 
        

        left = 0
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2
            if check(mid) <= k:
                right = mid - 1
            else:
                left = mid + 1
            
        return left 
    
# This has time complexity O(n log k), where n is the length of nums and k is the sum of nums
# and space complexity O(1)