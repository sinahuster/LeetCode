"""
Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

Constraints:
1 <= n <= 105
"""

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        if n == 1:
            return 1 
        
        concatenation = ""
        for i in range(1, n + 1):
            concatenation += bin(i)[2:]
            #print(concatenation)

        total = int(concatenation, 2)
        #print(total)

        return total % (pow(10, 9) + 7)
    

# This has time complexity O(n), where n is the input 
# and space complexity O(1)