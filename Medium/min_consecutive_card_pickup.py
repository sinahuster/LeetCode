"""
You are given an integer array cards where cards[i] represents the value of the ith card. 
A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. 
If it is impossible to have matching cards, return -1.

Constraints:
1 <= cards.length <= 10^5
0 <= cards[i] <= 10^6
"""

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        seen = {}
        matching = False
        shortest = len(cards)

        for i in range(len(cards)):
            if cards[i] in seen:
                matching = True
                shortest = min(shortest, i - seen[cards[i]] + 1)
            seen[cards[i]] = i

        if matching:
            return shortest 
        return -1 


"""
This has time complexity O(n) and space complexity O(n) where n is the length of 
"""