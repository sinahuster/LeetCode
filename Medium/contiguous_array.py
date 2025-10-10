"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = defaultdict(int)
        ans = total = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                total -= 1
            if nums[i] == 1:
                total += 1
            
            if total == 0:
                ans = i + 1
            elif total in count:
                ans = max(ans, i - count[total])
            else:
                count[total] = i

        return ans

# -1 for zeros, +1 for ones, when the total is 0, we have equal zeros and ones

# This has time and space complexity O(n)