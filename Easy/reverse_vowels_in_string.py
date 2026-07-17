"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Constraints:
1 <= s.length <= 3 * 10^5
s consist of printable ASCII characters.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        found = []
        position = []
        new = list(s)
        
        for i in range(len(s)):
            if s[i] in vowels:
                found.append(s[i])
                position.append(i)

        for pos in position:
            new[pos] = found.pop()

        return ''.join(new)
    
# This has time complexity O(n), where n is the length of s
# and space complexity O(n)