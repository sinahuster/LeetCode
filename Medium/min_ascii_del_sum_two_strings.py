"""
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Constraints:
1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @cache
        def dp(row, col):
            if col == len(s1):
                left = 0
                while row < len(s2):
                    left += ord(s2[row])
                    row += 1
                return left 
            if row == len(s2):
                left = 0
                while col < len(s1):
                    left += ord(s1[col])
                    col += 1
                return left 

            delete_col = ord(s1[col]) + dp(row, col + 1)
            delete_row = ord(s2[row]) + dp(row + 1, col)

            if s1[col] == s2[row]:
                keep = dp(row + 1, col + 1)
                return min(keep, delete_col, delete_row)

            return min(delete_row, delete_col)

        return dp(0,0)
    
    # This has time and space complexity O(n * m), where n and m are the lengths of s1 and s2 respectively 