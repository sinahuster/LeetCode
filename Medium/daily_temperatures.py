"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answers = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                    j = stack.pop()
                    answers[j] = i - j

            stack.append(i)

        return answers


# stack with highest temperature at the bottom 

# This has time complexity and space complexity O(n)
