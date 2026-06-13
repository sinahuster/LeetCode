"""
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

Constraints:
n == spells.length
m == potions.length
1 <= n, m <= 10^5
1 <= spells[i], potions[i] <= 10^5
1 <= success <= 10^10
"""

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        def binary_search(arr, target):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left  

        potions.sort()
        pairs = []
        m = len(potions)

        for spell in spells:
            non_success = binary_search(potions, success / spell)
            pairs.append(m - non_success)

        return pairs

# This has time complexity O((n + m) log m), where n is the length of spells and m is the length of potions,
# and space complexity O(n)