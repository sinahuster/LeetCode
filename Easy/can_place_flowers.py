"""
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Constraints:
1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        possible = 0
        last = -2
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                last = i 
            if i - last == 3:
                last = i - 1
                possible += 1
            if i == len(flowerbed) - 1 and i - last == 2:
                possible += 1

        return possible >= n
    
# This has time complexity O(m), where m is the length of flowerbed
# and space complexity O(1)