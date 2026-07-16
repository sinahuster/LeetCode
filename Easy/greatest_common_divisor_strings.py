"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        n = len(str1)
        m = len(str2)
        largest = ""
        max_len = min(m, n)

        for i in range(1, max_len + 1):
            if max_len % i == 0:
                num_one = int(n / i)
                num_two = int(m / i)
                substring = str2[:i]
                if str1 == num_one * substring and str2 == num_two * substring:
                    largest = substring

        return largest 
    
# This has time complexity O(min(n, m) * (n + m))
# and the space complexity is O(n + m)