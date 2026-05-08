"""
Given an array of integers arr and an integer k. 
Find the least number of unique integers after removing exactly k elements.

Constraints:
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        counts = Counter(arr)
        ordered = sorted(counts.values(), reverse=True)

        while k:
            val = ordered[-1]
            if val <= k:
                k -= val
                ordered.pop()
            else:
                break

        return len(ordered)
    


# This has time complexity O(n log n), where n is the length of arr, 
# and space complexity O(n)