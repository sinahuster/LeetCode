"""
You are given an integer array arr. 
You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Constraints:
2 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
"""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        #print(count)
        size = len(arr)
        new_size = size
        removed = 0

        for num, freq in count.most_common():
            if new_size <= size / 2:
                break       
            new_size -= freq
            removed += 1
            #print(num, removed, new_size)

        return removed


# This has time complexity of O(n log n), where n is the length of arr,
# and space complexity O(n)