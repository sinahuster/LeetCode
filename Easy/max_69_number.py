"""
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Constraints:
1 <= num <= 10^4
num consists of only 6 and 9 digits.
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]

        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break
            
        return int(''.join(map(str, digits)))
    

# This has time complexity O(d), where d is the number of digits in num,
# and space complexity O(d)