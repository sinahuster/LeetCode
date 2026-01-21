"""
You are given an array nums consisting of n prime integers.

You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], 
i.e. ans[i] OR (ans[i] + 1) == nums[i].

Additionally, you must minimize each value of ans[i] in the resulting array.

If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.

Constraints:
1 <= nums.length <= 100
2 <= nums[i] <= 10^9
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
                    count = -1
                    for j in range(len(bits) - 1, 0, -1):
                        if bits[j] == '0':
                            break
                        count += 1
                    factor = 2 ** count
                    ans[i] = nums[i] - factor                    

        return ans



# 101111 - 47
# 100111 - 39
# 101000 - 40
        

# This has time complexity O(n * log k), where n is the length of nums and k is the largest integer in nums
# and space complexity O(n)