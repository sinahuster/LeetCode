"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Constraints:
0 <= num <= 10^6
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        steps = 0

        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1

        return steps
    

# This has time complexity O(log n), where n is the size of the num,
# and space complexity O(1)