"""
You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Constraints:
n == nums.length
m == queries.length
1 <= n, m <= 1000
1 <= nums[i], queries[i] <= 10^6
"""

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        def binary_search(arr, target):
            left = 0
            right = m
            while left < right:
                mid = (left + right) // 2
                if arr[mid + 1] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        nums.sort()
        ans = []
        m = len(nums)
        sums = [0] * (m + 1)
        for i in range(m):
            sums[i + 1] = sums[i] + nums[i]

        for query in queries:
            ans.append(binary_search(sums, query))

        return ans
    
# This has time complexity O((n + m) log n), where n is the length of nums and m is the length of queries,
# and space complexity O(m n)