"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        front = [1]
        back = [1] * len(nums)

        for i in range(1, len(nums)):
            new = front[i - 1] * nums[i - 1]
            front.append(new)
        
        for i in range(len(nums) - 1, 0, -1):
            back[i - 1] = back[i] * nums[i]

        return [front[i] * back[i] for i in range(len(nums))]
    
# This has time complexity O(n)
# and space complexity O(n)