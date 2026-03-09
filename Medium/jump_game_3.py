"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

Constraints:
1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length
"""

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = {start}
        queue = deque([start])
        length = len(arr)

        def next_steps(index):
            poss = []
            if index + arr[index] < length:
                poss.append(index + arr[index])
            if index - arr[index] >= 0:
                poss.append(index - arr[index])
            return poss

        while queue:
            index = queue.popleft()
            if arr[index] == 0:
                return True
            for option in next_steps(index):
                if option not in seen:
                    seen.add(option)
                    queue.append(option)

        return False
    

# This has time complexity and space complexity O(n), where n is the length of the array