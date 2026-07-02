"""
Koko loves to eat bananas. 
There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Constraints:
1 <= piles.length <= 10^4
piles.length <= h <= 10^9
1 <= piles[i] <= 10^9
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / k)

            return hours <= h
    
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
    
# check runs with time complexity O(n), where n is the length of piles. 
# The binary search runs in O(log k), where k is max(piles). 
# So the total time complexity is O(n log k).
# And the space complxity is O(1) 