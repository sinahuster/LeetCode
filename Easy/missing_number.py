"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Constraints:
n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
All the numbers of nums are unique.

"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n + 1) * n // 2  
        return total - sum(nums)