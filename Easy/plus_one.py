"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        if digits[length - 1] < 9:
            digits[length -1] += 1
            return digits 
        
        digits = [0] + digits
        current = length
        while digits[current] == 9:
            digits[current] = 0
            current -= 1

        digits[current] += 1

        if digits[0] == 0:
            digits = digits[1:]

        return digits