"""
You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n - 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.

Constrants:
3 <= n <= 100
-1000 <= nums[i] <= 1000
"""

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        n = len(nums)
        swaps = [0]
        increasing = True
        if nums[1] <= nums[0]:
            return False 
        
        for i in range(1, n - 1):
            if nums[i] == nums[i + 1]:
                return False
            if increasing:
                if nums[i] > nums[i + 1]:
                    swaps.append(i)
                    increasing = False 
            else:
                if nums[i] < nums[i + 1]:
                    swaps.append(i)
                    increasing = True

        return len(swaps) == 3
    
# this has time complexity O(n), where n is the length of nums 
# and space comeplexity O(1)