"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Constraints:
1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = defaultdict(int)
        my_jewels = 0

        for stone in stones:
            count[stone] += 1
        
        for jewel in jewels:
            my_jewels += count[jewel]

        return my_jewels


"""
This has time complexity O(n + m), where n is the length of stones and m is the length of jewels. 
It has space cmplexity O(n), or O(k) where k is the size of the alphabet including upper and lowercase 
"""