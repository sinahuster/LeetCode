"""
You are given a string s consisting of lowercase English letters. 
A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. 
It can be proven that the answer is unique.

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
"""

class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

# This has time and space complexity O(n), where n is the length of the input 