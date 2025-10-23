"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack = []
            for c in string:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)
        
        return build(s) == build(t)

# This has time and space complexity O(n)