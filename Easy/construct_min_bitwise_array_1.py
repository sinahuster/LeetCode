"""
You are given an array nums consisting of n prime integers.

You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].

Additionally, you must minimize each value of ans[i] in the resulting array.

If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.

Constraints:
1 <= nums.length <= 100
2 <= nums[i] <= 1000
nums[i] is a prime number.
"""

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        ans = [-1] * len(nums)

        for i in range(len(nums)):
            if nums[i] != 2:
                bits = bin(nums[i])[2:]
                if '0' not in bits:
                    ans[i] = nums[i] // 2
                else:
                    for j in range(nums[i]):
                        if (j | (j + 1)) == nums[i]:
                            ans[i] = j
                            break
                    
        return ans

# This has time complexity O(n * M), where n is the size of the array nums and M is the maximum number in the aray 
# and space complexity O(n)