""" 
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Constraints:
1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = {}

        for c in sentence:
            if c not in seen:
                seen[c] = True 

        if len(seen) == 26:
            return True

        return False 