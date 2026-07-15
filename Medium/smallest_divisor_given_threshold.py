"""
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. 
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. 
(For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.

Constraints:
1 <= nums.length <= 5 * 10^4
1 <= nums[i] <= 10^6
nums.length <= threshold <= 10^6
"""

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def check(divisor):
            total = 0
            for num in nums:
                total += ceil(num / divisor)
            return total <= threshold
            
        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left 
    
# This has time complexity of O(n log k), where n is the length of nums, and k is max(nums)
# and it has space comeplexity of O(1)