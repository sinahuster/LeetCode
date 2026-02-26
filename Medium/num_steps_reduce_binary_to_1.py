"""
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.

Constraints:
1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'
"""

class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)

        steps = 0
        carry = 0
        for i in range(n - 1, 0, -1):
            digit = int(s[i]) + carry 
            if digit % 2 == 1:
                steps += 2
                carry = 1
            else:
                steps += 1

        return steps + carry 

# This has time complexity O(n), where n is the length of s 
# and space complexity O(1)