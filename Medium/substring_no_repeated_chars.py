"""
Given a string s, find the length of the longest substring without duplicate characters.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest = start = 0

        for end in range(len(s)):
            if s[end] in seen:
                while seen[s[end]] >= start:
                    start += 1
            seen[s[end]] = end
            longest = max(longest, end - start + 1)

        return longest 


"""
This has time and space complexity O(n), where n is the length of the string s. 
"""