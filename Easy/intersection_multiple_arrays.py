"""
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, 
return the list of integers that are present in each array of nums sorted in ascending order.

Constraints:
1 <= nums.length <= 1000
1 <= sum(nums[i].length) <= 1000
1 <= nums[i][j] <= 1000
All the values of nums[i] are unique.
"""

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        tally = defaultdict(int)

        for array in nums:
            for element in array:
                tally[element] += 1

        result = []
        n = len(nums)

        for key in tally:
            if tally[key] == n:
                result.append(key)

        return sorted(result)