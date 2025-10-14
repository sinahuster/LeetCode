"""
You are given a 0-indexed array nums consisting of positive integers. 
You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions. 
If no such pair of indices exists, return -1.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        pairs = {}
        largest = -1

        for num in nums:
            digits = sum([int(digit) for digit in str(num)])   
            if digits not in pairs:
                pairs[digits] = [-1, -1]

            first, second = pairs[digits]

            if num > first:
                second = first
                first = num

            elif num > second:
                second = num

            pairs[digits] = [first, second]


        for key in pairs:
            if pairs[key][0] != -1 and pairs[key][1] != -1:
                largest = max(largest, pairs[key][0] + pairs[key][1])
        
        return largest

"""
This has time and complexity O(n)
"""