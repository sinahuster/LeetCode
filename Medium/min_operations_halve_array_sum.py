"""
You are given an array nums of positive integers. 
In one operation, you can choose any number from nums and reduce it to exactly half the number. 
(Note that you may choose this reduced number in future operations.)

Return the minimum number of operations to reduce the sum of nums by at least half.

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^7
"""

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2

        heap = [-num for num in nums]
        heapq.heapify(heap)

        ans = 0 
        while target > 0:
            ans += 1
            x = heapq.heappop(heap)
            target += x / 2
            heapq.heappush(heap, x / 2)
        
        return ans
    

# This has time complexity O(n log n) and space complexity O(n).