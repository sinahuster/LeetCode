"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Constraints:
1 <= text.length <= 10^4
text consists of lower case English letters only.
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        balloon = []

        for char in text:
            count[char] += 1
        
        balloon.append(count["b"])
        balloon.append(count["a"])
        balloon.append(count["l"] // 2)
        balloon.append(count["o"] // 2)
        balloon.append(count["n"])

        return min(balloon)


# This has time complexity O(n) and space complexity O(n)