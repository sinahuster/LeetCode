"""
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the 
absolute difference between any two elements of this subarray is less than or equal to limit.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decreasing = deque()
        increasing = deque()
        valid = left = 0

        for right in range(len(nums)):
            # maintain monotonic decreasing and increasing deques
            while decreasing and nums[right] > nums[decreasing[-1]]:
                decreasing.pop()
            while increasing and nums[right] < nums[increasing[-1]]:
                increasing.pop()

            decreasing.append(right)
            increasing.append(right)

            # maintain the window property 
            while nums[decreasing[0]] - nums[increasing[0]] > limit:
                if nums[left] == nums[decreasing[0]]:
                    decreasing.popleft()
                if nums[left] == nums[increasing[0]]:
                    increasing.popleft()
                left += 1
            
            valid = max(valid, right - left + 1)

        return valid

# This has time and space complexity O(n)