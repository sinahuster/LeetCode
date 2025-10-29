"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""

from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a deque which allows removal from both ends of the queue
        window = deque()
        answer = []

        for i in range(len(nums)):
            # create a monotonic decreasing queue removing smaller elements from the queue 
            # as they have no chance of being the maximum 
            while window and nums[i] > nums[window[-1]]:
                window.pop()

            window.append(i)

            # if the window becomes too large, remove the left most element
            if window[0] + k == i:
                window.popleft()

            # start adding to asnwer once the window has reached size k
            if i >= k - 1:
                answer.append(nums[window[0]])

        return answer 


# This has time comlpexity O(n) where n is the size of nums, and space complexity O(k) where k is the window size 