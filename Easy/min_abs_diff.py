"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr

Constraints:
2 <= arr.length <= 10^5
-106 <= arr[i] <= 10^6
"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        min_diff = float("inf")
        mins = []

        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            if diff <= min_diff:
                if diff < min_diff:
                    mins = []
                mins.append([arr[i], arr[i + 1]])
                min_diff = diff

        return mins


# This has time and space complexity O(n)