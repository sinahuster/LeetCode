"""
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. 
There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. 
If such a character does not exist, return the first character in letters.

Constraints:
2 <= letters.length <= 10^4
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left = 0
        right = len(letters) - 1
        ans = -1

        while left <= right:
            mid = (right + left) // 2

            if letters[mid] > target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        if ans == -1:
            return letters[0]
        return letters[ans]
    

# This has time complexity O(log n) and space complexity O(1)