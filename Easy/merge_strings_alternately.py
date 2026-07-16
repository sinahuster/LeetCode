"""
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n = len(word1)
        m = len(word2)
        joint = ""

        for i in range(min(n,m)):
            joint += word1[i]
            joint += word2[i]
            
        if n <= m:
            joint += word2[n:]

        else:
            joint += word1[m:]

        return joint 
    

# This has time complexity O(k^2), where k is min(len(word1), len(word2))
# and space complexity O(len(word1) + len(word2))