"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Constraints:
1 <= ransomNote.length, magazine.length <= 10^5
ransomNote and magazine consist of lowercase English letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = defaultdict(int)

        for char in magazine:
            count[char] += 1

        for letter in ransomNote:
            count[letter] -= 1
            if count[letter] < 0:
                return False
        return True 

"""
This has time complexity O(n + m), where n is the length of magazine , and m is the length of ransonNote.
It has space complexity O(k), where k is the size of the alphabet. 
"""