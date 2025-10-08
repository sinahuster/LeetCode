"""
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = defaultdict(int)

        for char in s:
            count[char] += 1

        n = count[s[0]]

        for keys in count:
            if count[keys] != n:
                return False

        return True