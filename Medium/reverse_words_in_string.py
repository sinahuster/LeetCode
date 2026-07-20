"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.

Constraints:
1 <= s.length <= 10^4
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
"""

class Solution:
    def reverseWords(self, s: str) -> str:

        split_up = s.split(" ")
        words = []
        
        for i in range(len(split_up)):
            if split_up[i] != '':
                words.append(split_up[i])

        words.reverse()

        return " ".join(words)
    
# This has time complexity O(n), where n is the length of s 
# and space complexity O(n)
